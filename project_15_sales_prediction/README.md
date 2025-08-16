# Project 15: Sales Prediction

## Objective
The goal of this project is to build a model to predict sales for the Rossmann drug store chain. This project will involve time series analysis, feature engineering, and the development of a regression model to forecast future sales.

## Dataset
The dataset used for this project is a sample of the Rossmann Store Sales dataset from a Kaggle competition. It includes daily sales data for a subset of stores and includes information about promotions, holidays, and other relevant factors.

- **Source**: [Kaggle: Rossmann Store Sales](https://www.kaggle.com/c/rossmann-store-sales)
- **Data File**: `sales.csv` (a sample is included in this directory)

### Dataset Columns:
- `Store`: A unique Id for each store
- `DayOfWeek`: Day of the week (1=Monday, 7=Sunday)
- `Date`: The date of the sales record
- `Sales`: The turnover for any given day
- `Customers`: The number of customers on a given day
- `Open`: An indicator for whether the store was open (0 = closed, 1 = open)
- `Promo`: Indicates whether a store is running a promotion on that day
- `StateHoliday`: Indicates a state holiday (a = public holiday, b = Easter holiday, c = Christmas, 0 = None)
- `SchoolHoliday`: Indicates if the (Store, Date) was affected by the closure of public schools

## Project Plan
1.  **Data Loading and Initial Exploration**: Load the dataset and perform an initial review.
2.  **Data Cleaning and Preprocessing**:
    -   Handle the `StateHoliday` column, which has mixed data types.
    -   Convert the `Date` column to a datetime object.
    -   Extract time-based features from the `Date` column.
3.  **Exploratory Data Analysis (EDA)**:
    -   Analyze the relationship between sales and other features like promotions, holidays, and day of the week.
    -   Visualize sales trends over time.
4.  **Feature Engineering**:
    -   Create additional features that might influence sales.
    -   Encode categorical features as necessary.
5.  **Model Building and Training**:
    -   Split the data into training and testing sets.
    -   Implement and train a regression model (e.g., Linear Regression, Random Forest, or Gradient Boosting) to predict `Sales`.
6.  **Model Evaluation**:
    -   Evaluate the model's performance using metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
7.  **Conclusion**: Summarize the findings and the performance of the model.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
