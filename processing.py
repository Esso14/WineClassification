import pandas as pd
from pathlib import Path
from logger import logger, success
from utils import FileManager
from config import ConfigManager

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import mlflow
import joblib
import json
import os

# Import Classifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

os.chdir(Path(__file__).parent)

class DataProcess:
    def __init__(self, data_):
        self.data = data_
        self.df = None

        self.config = ConfigManager("config/config.json")

        self.data_path = (
            FileManager.create_folder_with_timestamp(
                self.config.get("data_folder_prefix")
            )
        )


    def processing(self):
        # ----- plit Data ---------
        X = self.data.data
        y = self.data.target

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        # Define Basis-Pipeline (with LogisticRegression as Standard-Classifier)
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', LogisticRegression())
        ])

        # Define Hyperparameter-Gitter (Param_Grid) for all Models
        # The 'classifier' notation ensures that the model is completely swapped out.
        # 'classifier__...' tunes the hyperparameters of the respective model.
        param_grid = [
                {
                    'classifier': [LogisticRegression(max_iter=1000)],
                    'classifier__solver': ["lbfgs"],
                    'classifier__C': [0.1, 1.0, 10.0]
                },
                {
                    'classifier': [DecisionTreeClassifier()],
                    'classifier__max_depth': [None, 5, 10]
                },
                {
                    'classifier': [RandomForestClassifier()],
                    'classifier__n_estimators': [50, 100, 200],
                },
                {
                    'classifier': [KNeighborsClassifier()],
                    'classifier__n_neighbors': [3, 5, 10],
                }
            ]

        grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
        grid_search.fit(X_train, y_train)

        # ==========================================
        # --------- EVALUATE RESULTS --------------#
        # ==========================================

        print("--- BEST RESULTS ---")
        print(f"Best Classifier: {grid_search.best_params_['classifier'].__class__.__name__}")
        print(f"Best Parameter: {grid_search.best_params_}")
        print(f"Best CV-Score: {grid_search.best_score_:.4f}")

        # Test the best model on the test data
        test_score = grid_search.score(X_test, y_test)
        print(f"Best model test-accuracy: {test_score:.4f}")

        # Display all tested combinations clearly in a DataFrame
        results_df = pd.DataFrame(grid_search.cv_results_)
        # Sort by best rank
        results_df = results_df.sort_values(by='rank_test_score')

        # Cleanup for better readability in Excel/CSV
        # (Extracts only the classifier name instead of the entire object)
        results_df["model_name"] = results_df["param_classifier"].apply(
            lambda x: x.__class__.__name__)

        # Select important columns and save as CSV
        export_cols = [
            "model_name",
            "mean_test_score",
            "std_test_score",
            "rank_test_score",
            "mean_fit_time",
        ]

        file_path = Path(self.data_path) / "pipeline_extract_results.csv"

        results_df[export_cols].to_csv(file_path, index=False, sep=";")
        success("Extract results were saved in 'pipeline_extract_results.csv'.")

        # ============================================
        # Save the best model (the finished pipeline)
        # ============================================

        # Extracts the entire pipeline (including StandardScaler and the best classifier)
        best_pipeline = grid_search.best_estimator_

        model_path = Path(self.data_path) / "best_ml_pipeline.joblib"
        # Save as a .joblib file (more efficient than Python's standard pickle)
        joblib.dump(best_pipeline, model_path)
        success("Best Model was saved as 'best_ml_pipeline.joblib' in the order data.")

        # ==========================================
        # Save the best metadata as JSON
        # ==========================================
        # Define which types are permitted directly within the JSON
        JSON_SAFE_TYPES = (int, float, str, bool, type(None))

        best_meta = {
            "best_classifier": best_pipeline.named_steps["classifier"].__class__.__name__,
            "best_parameter": {
                k: (v if isinstance(v, JSON_SAFE_TYPES) else v.__class__.__name__)
                for k, v in grid_search.best_params_.items()
            },
            "best_cv_accuracy": float(grid_search.best_score_),
            "test_accuracy": float(grid_search.score(X_test, y_test)),
        }

        json_path = Path(self.data_path) / "best_model_metadata.json"
        with open(json_path, "w") as f:
            json.dump(best_meta, f, indent=4)
        success("Metadata were saved in 'best_model_metadata.json' in order data.")

        print("\nTop 5 Modell-Kombinationen:")
        print(results_df[['param_classifier', 'mean_test_score', 'rank_test_score']].head())

