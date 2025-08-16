# Project 18: Credit Scoring

## Objective
The objective of this project is to develop a credit scoring model that can predict the creditworthiness of a loan applicant. This model will help in making decisions about whether to approve or deny a loan application, based on the applicant's financial and personal details.

## Dataset
The dataset used for this project is the "Credit Scoring" dataset. It contains various attributes of loan applicants, such as their income, assets, debt, and marital status, along with their credit status (good or bad).

- **Source**: [GitHub: gastonstat/CreditScoring](https://github.com/gastonstat/CreditScoring)
- **Data File**: `credit_scoring.csv` (included in this directory)

### Dataset Columns:
- `Status`: Credit status (1: good, 2: bad) - This is the target variable.
- `Seniority`: Job seniority in years
- `Home`: Type of home ownership
- `Time`: Time of requested loan
- `Age`: Client's age
- `Marital`: Marital status
- `Records`: Existance of records
- `Job`: Type of job
- `Expenses`: Amount of expenses
- `Income`: Amount of income
- `Assets`: Amount of assets
- `Debt`: Amount of debt
- `Amount`: Amount of requested loan
- `Price`: Price of the good

## Project Plan
1.  **Data Loading and Initial Exploration**: Load the dataset and perform an initial review of its structure and features.
2.  **Data Cleaning and Preprocessing**:
    -   Handle any missing or inconsistent values.
    -   Encode categorical variables as needed.
3.  **Exploratory Data Analysis (EDA)**:
    -   Analyze the distribution of the target variable (`Status`).
    -   Investigate the relationships between different attributes and credit status.
4.  **Model Building and Training**:
    -   Split the data into training and testing sets.
    -   Implement and train a classification model (e.g., Logistic Regression, Random Forest, or Gradient Boosting) to predict the credit status.
5.  **Model Evaluation**:
    -   Evaluate the model's performance using metrics such as accuracy, precision, recall, and F1-score.
    -   Analyze the confusion matrix to understand the model's prediction behavior.
6.  **Conclusion**: Summarize the model's performance and its potential for use in a real-world credit scoring system.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
