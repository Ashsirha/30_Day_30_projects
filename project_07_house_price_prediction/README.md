# Project 7: House Price Prediction

This project tackles the classic regression problem of predicting house prices based on various property features. We will use a simplified version of the Ames Housing dataset and compare the performance of a baseline Linear Regression model with a more advanced XGBoost model.

## 📜 Description

The notebook `house_price_prediction.ipynb` provides a complete regression workflow:
1.  **Data Loading & EDA:** Loads the sample housing data and explores the relationships between features like living area, overall quality, and the final sale price.
2.  **Feature Engineering:** Selects the most relevant features for the models.
3.  **Model Building:**
    *   **Baseline Model:** A simple Linear Regression model to establish a performance baseline.
    *   **Advanced Model:** An XGBoost Regressor, a powerful gradient boosting algorithm known for its high performance on tabular data.
4.  **Training & Evaluation:** Splits the data, trains both models, and evaluates their performance using standard regression metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.
5.  **Conclusion:** Compares the performance of the two models and discusses the key drivers of house prices found in the analysis.

This project covers the following key skills:
*   Regression Analysis
*   Feature Engineering & Selection
*   Model Evaluation for Regression
*   Linear Regression and XGBoost

## 💾 Dataset

This project includes a simplified, sample dataset named `train.csv`, located in the `data/` directory. It is based on the Ames Housing dataset and contains a subset of the most important features for predicting house prices.

**No data download is required.**

## 📁 Project Structure

```
project_07_house_price_prediction/
│
├── data/
│   └── train.csv  # Sample data included
│
├── house_price_prediction.ipynb  # Main analysis and regression notebook
├── requirements.txt              # Project dependencies
└── README.md                     # This file
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
3.  Open and run the `house_price_prediction.ipynb` notebook.
