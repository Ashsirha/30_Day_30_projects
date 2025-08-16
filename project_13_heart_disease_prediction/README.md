# Project 13: Heart Disease Prediction

## Objective
The objective of this project is to build a machine learning model to predict the presence of heart disease in a patient based on a set of medical attributes. This is a binary classification problem.

## Dataset
The dataset to be used is the "Heart Disease UCI" dataset, which is a popular dataset for classification tasks. It contains 14 attributes including age, sex, chest pain type, resting blood pressure, and more. The target variable is 'target', where 1 indicates the presence of heart disease and 0 indicates its absence.

- **Source**: [UCI Machine Learning Repository: Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Data File**: `heart.csv` (to be acquired)

### Dataset Columns:
- `age`: Age in years
- `sex`: (1 = male; 0 = female)
- `cp`: Chest pain type
- `trestbps`: Resting blood pressure (in mm Hg on admission to the hospital)
- `chol`: Serum cholestoral in mg/dl
- `fbs`: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
- `restecg`: Resting electrocardiographic results
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise induced angina (1 = yes; 0 = no)
- `oldpeak`: ST depression induced by exercise relative to rest
- `slope`: The slope of the peak exercise ST segment
- `ca`: Number of major vessels (0-3) colored by flourosopy
- `thal`: 3 = normal; 6 = fixed defect; 7 = reversable defect
- `target`: 1 or 0

## Project Plan
1.  **Data Loading and Initial Exploration**: Load the dataset and perform an initial review.
2.  **Data Cleaning and Preprocessing**: Handle any missing values and ensure data types are correct.
3.  **Exploratory Data Analysis (EDA)**: Analyze the relationships between different attributes and the target variable.
4.  **Model Building and Training**: Implement and train a classification model (e.g., Logistic Regression, Random Forest, or XGBoost).
5.  **Model Evaluation**: Evaluate the model's performance using metrics like accuracy, precision, recall, and F1-score.
6.  **Conclusion**: Summarize the findings.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
