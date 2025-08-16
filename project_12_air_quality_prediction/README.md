# Project 12: Air Quality Prediction

## Objective
The goal of this project is to analyze the Air Quality dataset from the UCI Machine Learning Repository and develop a model to predict air quality based on various sensor readings and environmental factors. This project will involve time series analysis, data preprocessing, feature engineering, and the implementation of a regression model.

## Dataset
The dataset contains responses from a gas multisensor device deployed on the field in a significantly polluted area, at road level, within an Italian city. Data were recorded from March 2004 to February 2005 (one year).

- **Source**: [UCI Machine Learning Repository: Air Quality Dataset](https://archive.ics.uci.edu/ml/datasets/Air+Quality)
- **Data File**: `AirQualityUCI.csv` (included in this directory)

### Dataset Columns:
- `Date`: Date (DD/MM/YYYY)
- `Time`: Time (HH.MM.SS)
- `CO(GT)`: True hourly averaged concentration CO in mg/m^3 (reference analyzer)
- `PT08.S1(CO)`: PT08.S1 (tin oxide) hourly averaged sensor response (nominally CO targeted)
- `NMHC(GT)`: True hourly averaged overall Non-Methane HydroCarbons concentration in microg/m^3 (reference analyzer)
- `C6H6(GT)`: True hourly averaged Benzene concentration in microg/m^3 (reference analyzer)
- `PT08.S2(NMHC)`: PT08.S2 (titania) hourly averaged sensor response (nominally NMHC targeted)
- `NOx(GT)`: True hourly averaged NOx concentration in ppb (reference analyzer)
- `PT08.S3(NOx)`: PT08.S3 (tungsten oxide) hourly averaged sensor response (nominally NOx targeted)
- `NO2(GT)`: True hourly averaged NO2 concentration in microg/m^3 (reference analyzer)
- `PT08.S4(NO2)`: PT08.S4 (tungsten oxide) hourly averaged sensor response (nominally NO2 targeted)
- `PT08.S5(O3)`: PT08.S5 (indium oxide) hourly averaged sensor response (nominally O3 targeted)
- `T`: Temperature in °C
- `RH`: Relative Humidity (%)
- `AH`: Absolute Humidity

**Note**: -200 is used as a placeholder for missing values in the dataset.

## Project Plan
1.  **Data Loading and Initial Exploration**: Load the dataset using Pandas and perform an initial inspection of its structure, columns, and data types.
2.  **Data Cleaning and Preprocessing**:
    -   Handle missing values (represented by -200).
    -   Combine `Date` and `Time` columns to create a proper datetime index.
    -   Correct data types, paying special attention to numerical columns with comma decimal separators.
    -   Drop any unnecessary columns.
3.  **Exploratory Data Analysis (EDA)**:
    -   Visualize the time series data for different pollutants to identify trends, seasonality, and anomalies.
    -   Analyze the relationships between different sensor readings and environmental factors using correlation matrices and pair plots.
4.  **Feature Engineering**:
    -   Extract time-based features from the datetime index (e.g., hour, day of the week, month).
    -   Create lag features to incorporate past sensor readings into the model.
5.  **Model Building and Training**:
    -   Split the data into training and testing sets based on a chronological order.
    -   Implement and train a regression model (e.g., Linear Regression, Random Forest, or a time-series specific model like ARIMA/SARIMA) to predict a target pollutant concentration (e.g., `C6H6(GT)`).
6.  **Model Evaluation**:
    -   Evaluate the model's performance on the test set using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.
    -   Visualize the predicted vs. actual values to assess the model's accuracy.
7.  **Conclusion**: Summarize the findings from the analysis and the performance of the predictive model.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
