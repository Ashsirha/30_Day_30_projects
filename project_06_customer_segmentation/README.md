# Project 6: Customer Segmentation

This project uses unsupervised machine learning techniques to perform customer segmentation. We will analyze a dataset of mall customers and group them into distinct clusters based on their annual income and spending score using the K-Means algorithm.

## 📜 Description

The notebook `customer_segmentation.ipynb` demonstrates a complete clustering workflow:
1.  **Data Loading & EDA:** Loads the sample customer data and visualizes the relationships between age, income, and spending score.
2.  **Feature Selection:** Selects the 'Annual Income' and 'Spending Score' features for clustering.
3.  **Finding the Optimal Number of Clusters:** Uses the Elbow Method to determine the best number of clusters (k) for the K-Means algorithm.
4.  **K-Means Modeling:** Trains a K-Means model with the optimal 'k' to segment the customers.
5.  **Visualizing Segments:** Creates a scatter plot to visualize the distinct customer segments, making the results easy to interpret.
6.  **Conclusion:** Analyzes the characteristics of each customer segment and discusses how a business could use this information for targeted marketing strategies.

This project covers the following key skills:
*   Unsupervised Learning
*   Clustering with K-Means
*   The Elbow Method for optimal 'k' selection
*   Data Visualization for Cluster Analysis
*   Exploratory Data Analysis (EDA)

## 💾 Dataset

This project includes a sample dataset, `Mall_Customers.csv`, located in the `data/` directory. It contains 200 rows of customer data with the following features: `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, and `Spending Score (1-100)`.

**No data download is required.**

## 📁 Project Structure

```
project_06_customer_segmentation/
│
├── data/
│   └── Mall_Customers.csv  # Sample data included
│
├── customer_segmentation.ipynb  # Main analysis and clustering notebook
├── requirements.txt             # Project dependencies
└── README.md                    # This file
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
3.  Open and run the `customer_segmentation.ipynb` notebook.
