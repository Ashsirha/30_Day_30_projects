# Project 28: Predictive Maintenance

## Objective
The objective of this project is to build a predictive maintenance model that can predict machine failure based on sensor data. This will help in identifying potential failures before they occur, allowing for proactive maintenance and reducing downtime.

## Dataset
This project uses the **AI4I 2020 Predictive Maintenance Dataset** from the UCI Machine Learning Repository. This synthetic dataset reflects real-world predictive maintenance data and includes various sensor readings and machine failure information.

- **Source**: [UCI Machine Learning Repository: AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/ml/datasets/ai4i+2020+predictive+maintenance+dataset)
- **Data File**: `ai4i2020.csv` (included in this directory)

### Dataset Columns:
- `UDI`: Unique identifier
- `Product ID`: ID of the product
- `Type`: Quality variant of the product (L, M, H)
- `Air temperature [K]`: Air temperature in Kelvin
- `Process temperature [K]`: Process temperature in Kelvin
- `Rotational speed [rpm]`: Rotational speed of the tool
- `Torque [Nm]`: Torque of the tool
- `Tool wear [min]`: Tool wear in minutes
- `Machine failure`: Label indicating if the machine failed (1) or not (0) - This is the target variable.
- `TWF`, `HDF`, `PWF`, `OSF`, `RNF`: Specific failure modes

## Project Plan
1.  **Data Loading and Initial Exploration**: Load the dataset and get an initial understanding of its structure.
2.  **Data Cleaning and Preprocessing**:
    -   Drop irrelevant columns (`UDI`, `Product ID`).
    -   Encode the categorical `Type` column.
3.  **Exploratory Data Analysis (EDA)**:
    -   Analyze the distribution of the `Machine failure` target variable.
    -   Explore the relationships between sensor readings and machine failure.
4.  **Model Building and Training**:
    -   Split the data into training and testing sets.
    -   Train a classification model, such as a Random Forest or Gradient Boosting, to predict `Machine failure`.
5.  **Model Evaluation**:
    -   Evaluate the model's performance using metrics like accuracy, precision, recall, and the F1-score, which are important for imbalanced datasets.
    -   Analyze the confusion matrix to understand the model's performance on each class.
6.  **Conclusion**: Summarize the model's performance and its potential for use in a predictive maintenance system.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
