# Project 22: Recommender System

## Objective
The objective of this project is to build a movie recommender system using the MovieLens dataset. We will implement a collaborative filtering model to recommend movies to users based on their past ratings.

## Dataset
This project uses the **MovieLens 1M** dataset, which contains 1 million ratings from 6040 users on 3900 movies. The dataset is available through the `tensorflow_datasets` library.

- **Source**: `tensorflow_datasets` (movielens/1m-ratings)
- **Data**: The data will be loaded directly within the notebook.

## Project Plan
1.  **Data Loading and Preparation**:
    -   Load the MovieLens 1M dataset using `tensorflow_datasets`.
    -   Extract the user IDs, movie titles, and ratings.
2.  **Model Building**:
    -   We will use a matrix factorization approach, which is a popular technique for collaborative filtering.
    -   Build a model using Keras that learns user and movie embeddings. The dot product of these embeddings will be used to predict the rating a user would give to a movie.
3.  **Model Compilation and Training**:
    -   Compile the model with a suitable loss function (e.g., Mean Squared Error) and an optimizer (e.g., Adam).
    -   Train the model on the user-movie-rating data.
4.  **Model Evaluation and Recommendation Generation**:
    -   Evaluate the model's performance by checking its ability to predict ratings.
    -   Implement a function that takes a user ID as input and recommends a list of movies that the user has not yet rated, based on the model's predictions.
5.  **Conclusion**:
    -   Summarize the performance of the recommender system and discuss its effectiveness in providing personalized movie recommendations.

## Technologies
- Python
- TensorFlow/Keras
- NumPy
- Matplotlib
- Jupyter Notebook
