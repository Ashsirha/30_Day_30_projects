# Project 14: Customer Churn Prediction

## Objective
The goal of this project is to build a model to predict customer churn for a bank. By analyzing customer data, we aim to identify the key factors that lead to a customer leaving the bank and develop a predictive model to identify customers at risk of churning.

## Dataset
The dataset used for this project is the "Churn Modelling" dataset from Kaggle. It contains information about bank customers, including their demographics, account details, and whether they have exited the bank.

- **Source**: [Kaggle: Churn Modelling Dataset](https://www.kaggle.com/datasets/sharmaroshan/churn-modelling-dataset)
- **Data File**: `churn.csv` (included in this directory)

### Dataset Columns:
- `RowNumber`: Row number
- `CustomerId`: Unique identifier for each customer
- `Surname`: Customer's surname
- `CreditScore`: Customer's credit score
- `Geography`: Customer's country (France, Spain, Germany)
- `Gender`: Customer's gender
- `Age`: Customer's age
- `Tenure`: Number of years the customer has been with the bank
- `Balance`: Customer's account balance
- `NumOfProducts`: Number of products the customer has with the bank
- `HasCrCard`: Whether the customer has a credit card (1 = yes, 0 = no)
- `IsActiveMember`: Whether the customer is an active member (1 = yes, 0 = no)
- `EstimatedSalary`: Customer's estimated salary
- `Exited`: Whether the customer has churned (1 = yes, 0 = no) - This is the target variable.

## Project Plan
1.  **Data Loading and Initial Exploration**: Load the dataset and perform an initial inspection to understand its structure and features.
2.  **Data Cleaning and Preprocessing**:
    -   Handle any missing values if present.
    -   Drop irrelevant columns (`RowNumber`, `CustomerId`, `Surname`).
    -   Encode categorical variables (`Geography`, `Gender`) into a numerical format.
3.  **Exploratory Data Analysis (EDA)**:
    -   Analyze the distribution of the target variable (`Exited`).
    -   Explore the relationships between different customer attributes and the likelihood of churning using visualizations.
4.  **Feature Engineering**:
    -   Standardize numerical features to ensure they are on a similar scale.
5.  **Model Building and Training**:
    -   Split the data into training and testing sets.
    -   Implement and train several classification models, such as Logistic Regression, Random Forest, and Gradient Boosting.
6.  **Model Evaluation**:
    -   Evaluate the models' performance using metrics like accuracy, precision, recall, F1-score, and the ROC-AUC score.
    -   Compare the performance of the different models to select the best one.
7.  **Conclusion**: Summarize the key findings and the performance of the final model.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
