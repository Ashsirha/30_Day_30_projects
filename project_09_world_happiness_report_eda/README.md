# Project 9: World Happiness Report EDA

This project performs an Exploratory Data Analysis (EDA) on the World Happiness Report data. The goal is to uncover insights into what factors are most correlated with happiness scores across different countries and regions. This is a data visualization and analysis project, not a predictive modeling one.

## 📜 Description

The notebook `world_happiness_eda.ipynb` provides a complete analysis workflow:
1.  **Data Loading & Inspection:** Loads the sample happiness data and performs an initial inspection of its structure and content.
2.  **Visualizing Top Countries:** Creates a bar chart to show the top 10 happiest countries based on their 'Ladder score'.
3.  **Distribution of Key Factors:** Uses histograms to visualize the distributions of the six key factors contributing to happiness (GDP, social support, life expectancy, freedom, generosity, corruption).
4.  **Correlation Analysis:**
    *   Uses scatter plots to explore the relationship between each factor and the overall happiness score.
    *   Generates a correlation heatmap to quantify the linear relationships between all variables.
5.  **Regional Analysis:** Compares average happiness scores across different world regions.
6.  **Conclusion:** Summarizes the key findings from the analysis, identifying the strongest drivers of happiness.

This project covers the following key skills:
*   Exploratory Data Analysis (EDA)
*   Data Visualization with Matplotlib and Seaborn
*   Correlation Analysis
*   Data Interpretation

## 💾 Dataset

This project includes a sample dataset, `world-happiness-report-2021.csv`, located in the `data/` directory. It is based on the 2021 World Happiness Report and contains a subset of countries and the key features for analysis.

**No data download is required.**

## 📁 Project Structure

```
project_09_world_happiness_report_eda/
│
├── data/
│   └── world-happiness-report-2021.csv  # Sample data included
│
├── world_happiness_eda.ipynb  # Main analysis and visualization notebook
├── requirements.txt           # Project dependencies
└── README.md                  # This file
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
3.  Open and run the `world_happiness_eda.ipynb` notebook.
