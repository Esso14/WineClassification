# Wine Classification with scikitlearn

This Project demonstrates how to work on the **Wine dataset** to classify types of wine using the **scikit-learn** library in Python. Four different machine learning classification algorithms will be apply on the wine dataset to train and evaluate a resulting model:
    - Logistic Regression, 
    - Decision Tree, 
    - Random Forest und 
    - K-Nearest Neighbors (KNN)

The results are stored in an SQLite database

---

### Features:
- **Load Wine dataset from scikit-learn and Quality check**
- **Create a data profile report** which includes statistics of the features, such as mean, median, range, and standard deviation using the Data Profiler
- **Data Preprocessing:**
  - Handle missing values if any
  - Perform feature scaling or normalization if necessary
  - Split the dataset into training and testing sets
- **Model Training with Cross-Validation**
  - ensure that the model doesn't overfit
  - Evaluate model performance using appropriate metrics (e.g., accuracy).
- **Hyperparameter Tuning with GridSearch:** Utilize **GridSearchCV** for hyperparameter tuning to improve model performance
- **Logging:** log important steps of the data processing and model training phases
- **Configuration Management**
- **Results Storage:** the results from different training phases will be into an SQLite database
- **Model Persistence:** Save the trained models using both **pickle** and **Joblib** for later use or deployment
- **Project Organization**
  - For each training cycle starts, create a new folder with the current date and time to store all results (data profiles, models, SQLite database, etc.).
  - ...

---

## Project Structure
<pre>
WineClassification/
│
├── config/
│   └── config.json
│   └── 
│
├── csv_files/
│   └── dataset.csv
│   └── dataset_scaled.csv
│ 
├── training_results/
│   └── data_process_<date-time>
│   └── model
│   └── model.db
│
├── logs/
│   └── app.log
│
├── app.py
├── config.py
├── db.py
├── profile.py
├── processing.py
├── .gitignore
├── README.md
└── requirements.txt

</pre>
---

## Database Schema

### Table
---

## Installation & Setup

---

## Running the project

---

## Technologie used

- Python 3.x
- SQLite
- Objektorientiertes Design

---

## License

This project is free to use and can be extended as needed