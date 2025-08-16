# Project 3: Stock Price Prediction

This project explores time series forecasting to predict stock prices. We will use two different models, ARIMA and LSTM, to forecast the future price of a stock and compare their performance.

## 📜 Description

The notebook `stock_price_prediction.ipynb` provides a complete workflow for time series analysis and forecasting:
1.  **Data Acquisition:** Fetches historical stock data using the `yfinance` library.
2.  **Exploratory Data Analysis (EDA):** Visualizes the stock's price history, trading volume, and moving averages to identify trends and patterns.
3.  **ARIMA Modeling:** Implements a traditional statistical model (Autoregressive Integrated Moving Average) for forecasting.
4.  **LSTM Modeling:** Implements a deep learning model (Long Short-Term Memory) for forecasting, which is well-suited for sequence prediction.
5.  **Evaluation:** Compares the predictions from both models against the actual stock prices.

This project covers the following key skills:
*   Time Series Analysis
*   Forecasting with ARIMA and LSTMs
*   Data Visualization with Matplotlib and Seaborn
*   Deep Learning with TensorFlow/Keras
*   Data Acquisition via APIs (`yfinance`)

## 💾 Dataset

This project does not require manual data download. The historical stock data is fetched dynamically from Yahoo Finance using the `yfinance` Python library within the notebook. By default, the notebook is configured to download data for Apple Inc. (ticker: `AAPL`), but this can be easily changed to any other stock ticker.

## 📁 Project Structure

```
project_03_stock_price_prediction/
│
├── stock_price_prediction.ipynb  # Main analysis and forecasting notebook
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
3.  Open and run the `stock_price_prediction.ipynb` notebook. The notebook will automatically download the required data.
