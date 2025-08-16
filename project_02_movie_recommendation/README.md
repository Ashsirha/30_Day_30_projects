# Project 2: Movie Recommendation System

This project builds a simple item-based collaborative filtering recommender system using the MovieLens 100k dataset. The goal is to recommend movies to users based on the ratings of similar movies.

## 📜 Description

The notebook `movie_recommendation.ipynb` walks through the process of:
1.  Loading and exploring the MovieLens 100k dataset.
2.  Performing Exploratory Data Analysis (EDA) to understand the data.
3.  Building an item-based collaborative filtering model.
4.  Creating a function to generate movie recommendations for a given movie.

This project covers the following key skills:
*   Recommender Systems
*   Collaborative Filtering
*   Similarity Metrics (Pearson Correlation)
*   Exploratory Data Analysis (EDA)
*   Data Handling with Pandas

## 💾 Dataset

The project uses the **MovieLens 100k Dataset**, which contains 100,000 ratings from 1,000 users on 1,700 movies.

*   **Source:** [GroupLens Website](https://grouplens.org/datasets/movielens/100k/)
*   **Direct Download:** [ml-100k.zip](https://files.grouplens.org/datasets/movielens/ml-100k.zip)

### Data Acquisition

1.  Download the dataset from the link above.
2.  Unzip the file `ml-100k.zip`.
3.  Place the `u.data` and `u.item` files into the `data/` directory within this project's folder.

## 📁 Project Structure

```
project_02_movie_recommendation/
│
├── data/
│   ├── u.data        # User ratings data (must be downloaded)
│   └── u.item        # Movie information (must be downloaded)
│
├── movie_recommendation.ipynb  # Main analysis and recommendation notebook
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

## 🚀 How to Run

1.  **Set up the environment:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Download the data:** Make sure you have downloaded the data and placed it in the `data/` folder as described above.
3.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
4.  Open and run the `movie_recommendation.ipynb` notebook.
