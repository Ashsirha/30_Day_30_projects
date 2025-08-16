# Project 20: Sentiment Analysis of Movie Reviews

## Objective
The objective of this project is to build a model that can classify movie reviews as either positive or negative. This is a classic binary text classification problem in the field of Natural Language Processing (NLP).

## Dataset
This project uses the **IMDb movie review sentiment classification dataset**, which is available directly from the `keras.datasets` module. This dataset contains 25,000 movie reviews for training and 25,000 for testing. The reviews are pre-processed and encoded as sequences of word indexes.

- **Source**: `keras.datasets.imdb`
- **Data**: The data will be loaded directly within the notebook.

## Project Plan
1.  **Data Loading and Preparation**:
    -   Load the IMDb dataset from `keras.datasets`.
    -   The data is already pre-processed, but we will need to pad the sequences to ensure they are all of the same length for input into a neural network.
2.  **Model Building and Training**:
    -   Build a sequential neural network model using Keras. The model will consist of:
        -   An `Embedding` layer to learn word embeddings for the vocabulary.
        -   A `GlobalAveragePooling1D` layer to reduce the dimensionality of the data.
        -   A `Dense` hidden layer with a ReLU activation function.
        -   A `Dense` output layer with a sigmoid activation function for binary classification.
3.  **Model Compilation and Training**:
    -   Compile the model with an Adam optimizer and binary cross-entropy loss function.
    -   Train the model on the training data, using a portion of it for validation.
4.  **Model Evaluation**:
    -   Evaluate the trained model on the test set to assess its performance.
    -   Plot the training and validation accuracy and loss over epochs to check for overfitting.
5.  **Conclusion**:
    -   Summarize the performance of the neural network model and its effectiveness in classifying the sentiment of movie reviews.

## Technologies
- Python
- TensorFlow/Keras
- NumPy
- Matplotlib
- Jupyter Notebook
