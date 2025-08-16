# Project 29: Anomaly Detection

## Objective
The objective of this project is to build an anomaly detection model using the Iris dataset. We will treat one of the classes as an anomaly and train a model to distinguish it from the other two classes. This will demonstrate the use of an Isolation Forest, a popular algorithm for anomaly detection.

## Dataset
This project uses the **Iris** dataset, which is a classic dataset in machine learning and is available directly from the `scikit-learn` library. The dataset contains 150 samples of iris flowers, each with four features.

- **Source**: `sklearn.datasets.load_iris`
- **Data**: The data will be loaded directly within the notebook.
- **Anomaly Definition**: For this project, we will consider the 'setosa' class as the normal data and a mix of 'versicolor' and 'virginica' as anomalies.

## Project Plan
1.  **Data Loading and Preparation**:
    -   Load the Iris dataset from `scikit-learn`.
    -   Prepare the data by creating a binary target variable where one class is treated as an anomaly.
2.  **Model Building and Training**:
    -   We will use the `IsolationForest` algorithm from `scikit-learn`, which is an effective model for anomaly detection.
    -   Train the Isolation Forest model on the prepared dataset.
3.  **Model Evaluation**:
    -   Evaluate the model's performance by checking its ability to correctly identify the anomalous data points.
    -   We will use metrics such as precision, recall, and the F1-score to assess the model's performance.
    -   Visualize the results to see how well the model separates the normal data from the anomalies.
4.  **Conclusion**:
    -   Summarize the performance of the Isolation Forest model and its effectiveness in detecting anomalies in the Iris dataset.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
