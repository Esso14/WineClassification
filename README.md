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
├── data/
│   └── data_process_<date-time>
│        └── best_ml_model.joblib
│        └── best_model_metadata.json
│        └── df_file.csv
│        └── pipeline_exatract_results.csv
│        └── profile_report.txt
│        └── profile.html
│        └── 
│
├── logs/
│   └── app.log
│
├── app_process.py
├── config.py
├── app.py
├── utils.py
├── profiler.py
├── logger.py
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

### 1. Clone the repository

`git clone <https://github.com/Esso14/WineClassification>`

---

## Running the project:

A new folder with the current date and timestamp will be create for each running to store all results (folder exemple: data_process_2026-06-12_120420)

### Generate and save a CSV file 
  `python3 app_process.py generate-csv`  --> df_file.csv

### Generate, save and profile a CSV file
  `python3 app_process.py profile-csv`   --> df_file.csv, profile_report.txt and profile.html

### Fit and save model + Generate, save and profile a CSV file
  `python3 app_process.py profile-csv`   --> report and joblib-model

---

## Test the wine classification App
  - Single wine 
  - Batch prediction (csv fil upload)

  [Start Wine Classification App](https://wineclassificationapp-ncpwacjpv5syeemp3kxbfo.streamlit.app)
  
---

## Technologie used

- Python 3.x
- SQLite
- Objektorientiertes Design

---

## License

This project is free to use and can be extended as needed