# Project 10: COVID-19 Cases Time Series Analysis

This project performs a time-series analysis and visualization of the global COVID-19 pandemic data. The goal is to process and explore the data to understand the trends, identify major waves, and compare the progression of the pandemic across different countries.

## 📜 Description

The notebook `covid19_time_series.ipynb` provides a complete analysis workflow:
1.  **Data Loading & Preprocessing:** Loads the time-series data for global confirmed cases from the Johns Hopkins University dataset. It then cleans and preprocesses the data by parsing dates, aggregating global numbers, and calculating daily new cases from cumulative data.
2.  **Global Trend Analysis:** Visualizes the pandemic's progression at a global level by plotting:
    *   Total confirmed cases over time.
    *   Daily new cases, which shows the raw daily volatility.
    *   A 7-day rolling average of new cases to smooth out the noise and clearly identify the major waves of the pandemic.
3.  **Country-Specific Comparison:** Compares the pandemic's trajectory in several key countries by plotting their respective 7-day rolling averages for new cases.
4.  **Conclusion:** Summarizes the key insights and trends observed from the visualizations.

This project covers the following key skills:
*   Time Series Analysis with Pandas
*   Data Wrangling and Preprocessing
*   Data Visualization for Time Series
*   Calculating and Visualizing Rolling Averages

## 💾 Dataset

This project uses the **COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University**. Specifically, we use the time-series data for global confirmed cases.

The notebook can load the data directly from the GitHub repository, but for reproducibility, it's recommended to download the file and place it in the `data/` directory.

*   **Data Source:** [JHU CSSE COVID-19 GitHub Repository](https://github.com/CSSEGISandData/COVID-19)
*   **Direct Download Link for Confirmed Cases:** [time_series_covid19_confirmed_global.csv](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv)

### Data Acquisition

1.  Click the direct download link above to get the CSV file.
2.  Place this CSV file inside the `data/` directory within this project's folder.

## 📁 Project Structure

```
project_10_covid19_time_series/
│
├── data/
│   └── time_series_covid19_confirmed_global.csv  # Must be downloaded
│
├── covid19_time_series.ipynb  # Main analysis and visualization notebook
├── requirements.txt           # Project dependencies
└── README.md                  # This file
```

## 🚀 How to Run

1.  **Set up the environment:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Download the data:** Make sure you have downloaded and placed the data file in the `data/` folder as described above.
3.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
4.  Open and run the `covid19_time_series.ipynb` notebook.
