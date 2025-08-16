# Project 5: Sentiment Analysis on Twitter Data

This project builds a deep learning model to classify the sentiment of tweets as either positive or negative. We will use a classic NLP dataset, Sentiment140, which contains 1.6 million tweets.

## 📜 Description

The notebook `sentiment_analysis_twitter.ipynb` walks through a complete NLP workflow:
1.  **Data Loading:** Loads the Sentiment140 dataset from a CSV file.
2.  **Text Preprocessing:** Cleans the raw tweet text by removing URLs, user mentions, punctuation, and stopwords.
3.  **EDA:** Visualizes the most frequent words in positive and negative tweets using word clouds.
4.  **Feature Engineering:** Converts the cleaned text into numerical sequences and pads them to a uniform length.
5.  **Model Building:** Constructs a sequential model using TensorFlow/Keras, featuring an `Embedding` layer and an `LSTM` layer to process the text data.
6.  **Model Training & Evaluation:** Trains the model on the dataset and evaluates its performance using accuracy, a confusion matrix, and a classification report.

This project covers the following key skills:
*   Natural Language Processing (NLP)
*   Text Preprocessing and Cleaning
*   Word Embeddings
*   Recurrent Neural Networks (LSTMs) for sequence classification
*   Data Visualization with Word Clouds

## 💾 Dataset

This project uses the **Sentiment140 dataset**. It contains 1,600,000 tweets extracted using the Twitter API. The tweets have been annotated (0 = negative, 2 = neutral, 4 = positive), and we will use the positive and negative tweets for this binary classification task.

*   **Direct Download Link:** [training.1600000.processed.noemoticon.csv.zip](https://nyc3.digitaloceanspaces.com/ml-files-distro/v1/sentiment-analysis-is-bad/data/training.1600000.processed.noemoticon.csv.zip)

### Data Acquisition

1.  Click the download link above to get the zip file.
2.  Unzip the downloaded file to get `training.1600000.processed.noemoticon.csv`.
3.  Place this CSV file inside the `data/` directory within this project's folder.

## 📁 Project Structure

```
project_05_sentiment_analysis_twitter/
│
├── data/
│   └── training.1600000.processed.noemoticon.csv  # Must be downloaded
│
├── sentiment_analysis_twitter.ipynb  # Main analysis and classification notebook
├── requirements.txt                  # Project dependencies
└── README.md                         # This file
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
4.  Open and run the `sentiment_analysis_twitter.ipynb` notebook.
