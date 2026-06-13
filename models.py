
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


class ModelFactory:

    MODEL_MAPPING = {
        "logistic_regression": LogisticRegression,
        "decision_tree": DecisionTreeClassifier,
        "random_forest": RandomForestClassifier,
        "knn": KNeighborsClassifier
    }

    @classmethod
    def create_model(cls, model_name: str, params: dict = None):

        if model_name not in cls.MODEL_MAPPING:
            raise ValueError(
                f"Model '{model_name}' is not supported."
            )

        params = params or {}

        return cls.MODEL_MAPPING[model_name](**params)
    


    #--- Cross-Validation-Models---------
    @classmethod
    def create_cv_models(cls, cv_config: dict):

        models = {}

        for model_name, params in cv_config.items():
            models[model_name] = cls.create_model(
                model_name,
                params
            )

        return models
    
    #---- Grid search models ------- 
    @classmethod
    def create_grid_search_models(cls, gs_config: dict):

        result = {}

        for model_name, cfg in gs_config.items():

            result[model_name] = {
                "model": cls.create_model(model_name),
                "param_grid": cfg["param_grid"]
            }

        return result