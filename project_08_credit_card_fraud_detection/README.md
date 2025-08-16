# Project 8: Credit Card Fraud Detection

This project tackles the critical and challenging problem of credit card fraud detection. The primary focus is on handling a highly imbalanced dataset, a common scenario in fraud detection where fraudulent transactions are very rare compared to legitimate ones.

## 📜 Description

The notebook `credit_card_fraud.ipynb` provides a complete workflow for this classification task:
1.  **Data Loading:** Fetches a credit card fraud dataset directly from the `imbalanced-learn` library.
2.  **EDA:** Analyzes the severe class imbalance and explores the anonymized features.
3.  **Data Preprocessing:** Scales the 'Amount' feature to ensure all features have a similar magnitude.
4.  **Handling Imbalanced Data:** Demonstrates the use of **Random Undersampling** to create a balanced training set. This technique is crucial for preventing the model from being biased towards the majority class.
5.  **Model Training:** Trains a Logistic Regression model on the balanced data.
6.  **Evaluation:** Evaluates the model's performance on the original, imbalanced test set using appropriate metrics for this task: the **Confusion Matrix**, **Classification Report (Precision, Recall, F1-score)**, and the **Precision-Recall Curve**.

This project covers the following key skills:
*   Handling Imbalanced Datasets
*   Random Undersampling
*   Fraud Detection Logic
*   Precision-Recall Trade-off
*   Classification Metrics for Imbalanced Data

## 💾 Dataset

This project uses a credit card fraud dataset provided by the `imbalanced-learn` Python library. The dataset is fetched automatically within the notebook.

**No data download is required.**

## 📁 Project Structure

```
project_08_credit_card_fraud_detection/
│
├── credit_card_fraud.ipynb  # Main analysis and classification notebook
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

## 🚀 How to Run

1.  **Set up the environment:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
3.  Open and run the `credit_card_fraud.ipynb` notebook. The notebook will automatically fetch the required data.
