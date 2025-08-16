# Project 23: Credit Card Fraud Detection

## Objective
The objective of this project is to build a machine learning model to detect fraudulent credit card transactions. This is a classic example of an imbalanced classification problem, where the number of fraudulent transactions is very small compared to the number of legitimate transactions.

## Dataset
This project uses the **Credit Card Fraud Detection** dataset, which is available from the `imbalanced-learn` library. This dataset is a modified version of the one from Kaggle, and it is well-suited for demonstrating techniques to handle imbalanced data.

- **Source**: `imblearn.datasets.fetch_datasets`
- **Data**: The data will be loaded directly within the notebook.

### Dataset Features:
The dataset contains 30 features, which are principal components obtained with PCA, and a 'Class' feature indicating whether a transaction is fraudulent (1) or not (0).

## Project Plan
1.  **Data Loading and Preparation**:
    -   Load the credit card fraud dataset using `imbalanced-learn`.
2.  **Exploratory Data Analysis (EDA)**:
    -   Analyze the class distribution to understand the extent of the imbalance.
    -   Visualize the feature distributions for both fraudulent and non-fraudulent transactions.
3.  **Handling Class Imbalance**:
    -   Implement a strategy to handle the imbalanced dataset, such as using the Synthetic Minority Over-sampling Technique (SMOTE) to generate synthetic samples for the minority class (fraudulent transactions).
4.  **Model Building and Training**:
    -   Split the data into training and testing sets.
    -   Train a classification model, such as Logistic Regression or a Random Forest, on the balanced training data.
5.  **Model Evaluation**:
    -   Evaluate the model's performance on the test set using metrics appropriate for imbalanced classification, including:
        -   Precision-Recall Curve
        -   Area Under the ROC Curve (AUC-ROC)
        -   Confusion Matrix
6.  **Conclusion**:
    -   Summarize the model's performance and the effectiveness of the chosen strategy for handling class imbalance.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- Jupyter Notebook
