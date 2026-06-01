# Task 1: Titanic Survival Prediction

This project builds a machine learning model to predict whether a passenger on the Titanic survived the disaster or not, based on demographic and ticketing data.

## Dataset Overview
The dataset contains information about individual passengers, including:
* **Survived:** Target variable (0 = No, 1 = Yes)
* **Pclass:** Ticket class (1st, 2nd, 3rd)
* **Sex & Age:** Passenger demographics
* **SibSp & Parch:** Family relation counts
* **Fare:** Price paid for the ticket
* **Embarked:** Port of embarkation

## Key Data Insights Discovered
Before building the model, an Exploratory Data Analysis (EDA) revealed:
* **Gender Factor:** ~74.20% of female passengers survived, compared to only ~18.89% of male passengers.
* **Class Factor:** ~62.96% of 1st class passengers survived, while only ~24.24% of 3rd class passengers survived.

##  Data Preprocessing Pipeline
To prepare the data for machine learning, the following steps were taken:
1. **Missing Data Imputation:** Handled missing data by filling blank `Age` and `Fare` rows with their respective column medians. Missing `Embarked` values were filled with 'S' (the most common port).
2. **Feature Removal:** Dropped the `Cabin` column because over 75% of its data was missing. Removed `Name`, `Ticket`, and `PassengerId` as they don't correlate to survival.
3. **Categorical Encoding:** Mapped text values to numbers (`Sex` -> male: 0, female: 1; `Embarked` -> S: 0, C: 1, Q: 2).

##  Model & Performance
* **Algorithm Used:** Random Forest Classifier (100 estimators)
* **Validation Accuracy:** **82.12%**
* **Outputs:** The final predictions for the unseen testing data have been successfully exported to `predictions.csv`.

## How to Run
1. Make sure you have the required libraries installed:
   ```bash
   pip install pandas scikit-learn
