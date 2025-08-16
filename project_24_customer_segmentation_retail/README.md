# Project 24: Customer Segmentation for Retail

## Objective
The objective of this project is to segment customers of an online retail store based on their purchasing behavior. We will use RFM (Recency, Frequency, Monetary) analysis and K-Means clustering to group customers into distinct segments.

## Dataset
The dataset used for this project is a sample of the "Online Retail" dataset from the UCI Machine Learning Repository. It contains transactional data from a UK-based online retail company.

- **Source**: [UCI Machine Learning Repository: Online Retail Data Set](http://archive.ics.uci.edu/ml/datasets/Online+Retail)
- **Data File**: `online_retail.csv` (a sample is included in this directory)

### Dataset Columns:
- `InvoiceNo`: Invoice number. A 6-digit integral number uniquely assigned to each transaction.
- `StockCode`: Product (item) code. A 5-digit integral number uniquely assigned to each distinct product.
- `Description`: Product (item) name.
- `Quantity`: The quantities of each product (item) per transaction.
- `InvoiceDate`: Invoice Date and time.
- `UnitPrice`: Unit price.
- `CustomerID`: Customer number. A 5-digit integral number uniquely assigned to each customer.
- `Country`: Country name.

## Project Plan
1.  **Data Loading and Initial Exploration**: Load the dataset and perform an initial review.
2.  **Data Cleaning and Preprocessing**:
    -   Handle missing values, especially in the `CustomerID` column.
    -   Remove returns (invoices with negative quantity).
    -   Calculate the total price for each transaction.
3.  **RFM Analysis**:
    -   Calculate Recency, Frequency, and Monetary values for each customer.
    -   Create RFM segments based on quartiles.
4.  **K-Means Clustering**:
    -   Use the Elbow method to determine the optimal number of clusters.
    -   Apply K-Means clustering to the RFM values to segment customers.
5.  **Segment Analysis and Visualization**:
    -   Analyze the characteristics of each customer segment.
    -   Visualize the segments to understand their distribution.
6.  **Conclusion**: Summarize the findings and discuss how the customer segments can be used for targeted marketing.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
