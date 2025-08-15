# Project 1: Titanic Survival Classification

This project builds a series of models to predict whether a passenger on the RMS Titanic survived the shipwreck. It serves as a classic introduction to machine learning classification.

## Dataset

The data for this project comes from the Kaggle competition **"Titanic - Machine Learning from Disaster"**.

*   **Source:** [Kaggle Competition Page](https://www.kaggle.com/competitions/titanic)
*   **Description:** The dataset provides a list of passengers (`train.csv`) with details like age, class, sex, and whether they survived. A second file (`test.csv`) contains passenger information without the survival label, which our model will predict.
*   **License:** The dataset's use is subject to the competition's rules, as outlined on the Kaggle page.

### Data Acquisition

To use this project, you must download the data from Kaggle and place it in the `data/` directory.

1.  Navigate to the [Kaggle data download page](https://www.kaggle.com/c/titanic/data).
2.  You will need a Kaggle account to download the files.
3.  Download `train.csv` and `test.csv`.
4.  Place both files inside the `project_01_titanic_survival/data/` directory.

## Project Structure

```
project_01_titanic_survival/
│
├── data/
│   ├── train.csv      # Must be downloaded from Kaggle
│   └── test.csv       # Must be downloaded from Kaggle
│
├── titanic_survival_classification.ipynb  # Main analysis notebook
├── requirements.txt                       # Project dependencies
└── README.md                              # This file
```

## How to Run

1.  **Clone the repository and navigate to the project directory.**

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```

5.  Open and run the `titanic_survival_classification.ipynb` notebook to see the analysis.
