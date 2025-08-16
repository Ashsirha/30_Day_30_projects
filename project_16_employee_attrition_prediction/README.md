# Project 16: Employee Attrition Prediction

## Objective
The goal of this project is to analyze the IBM HR Analytics Employee Attrition & Performance dataset to identify key factors contributing to employee attrition. We will build a predictive model to determine whether an employee is likely to leave the company.

## Dataset
The dataset used for this project is the "IBM HR Analytics Employee Attrition & Performance" dataset, which contains a variety of features about employees, such as their job role, satisfaction level, and personal demographics.

- **Source**: [Kaggle: IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **Data File**: `employee_attrition.csv` (included in this directory)

### Key Dataset Columns:
- `Age`: Age of the employee
- `Attrition`: Whether the employee has attrited (Yes/No) - This is the target variable.
- `BusinessTravel`: Frequency of business travel
- `Department`: Department the employee works in
- `DistanceFromHome`: Distance from home to work
- `EducationField`: Field of education
- `JobSatisfaction`: Job satisfaction level (1-4)
- `MaritalStatus`: Marital status of the employee
- `MonthlyIncome`: Monthly income of the employee
- `OverTime`: Whether the employee works overtime (Yes/No)
- `YearsAtCompany`: Number of years the employee has been with the company

## Project Plan
1.  **Data Loading and Initial Exploration**: Load the dataset and get an initial understanding of its structure and content.
2.  **Data Cleaning and Preprocessing**:
    -   Handle any missing values.
    -   Encode categorical variables into a numerical format suitable for machine learning models.
3.  **Exploratory Data Analysis (EDA)**:
    -   Analyze the distribution of the target variable (`Attrition`).
    -   Visualize the relationships between different employee attributes and attrition to identify key drivers.
4.  **Feature Engineering**:
    -   Scale numerical features to a common range.
5.  **Model Building and Training**:
    -   Split the data into training and testing sets.
    -   Implement and train various classification models (e.g., Logistic Regression, Random Forest, Gradient Boosting).
6.  **Model Evaluation**:
    -   Evaluate the models using metrics such as accuracy, precision, recall, and the F1-score.
    -   Select the best-performing model for predicting employee attrition.
7.  **Conclusion**: Summarize the insights gained from the analysis and the final model's performance.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
