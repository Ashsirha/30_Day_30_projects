# Project 11: Fake News Detection

This project builds a machine learning model to detect fake news. Using a dataset of real and fake news articles, we will train a classifier to distinguish between the two based on their text content. This is a classic text classification problem in NLP.

## 📜 Description

The notebook `fake_news_detection.ipynb` demonstrates a complete text classification workflow:
1.  **Data Loading & Preparation:** Loads the sample `Fake.csv` and `True.csv` files, adds a label to each, and combines them into a single, shuffled dataframe.
2.  **Text Preprocessing:** Cleans the article text by converting it to lowercase and removing punctuation and stopwords.
3.  **Feature Engineering with TF-IDF:** Converts the cleaned text into a matrix of TF-IDF features. This technique represents the importance of words in the articles, which is a powerful feature for text classification.
4.  **Model Training:** Trains a `PassiveAggressiveClassifier`, an efficient and effective algorithm for this type of text-based task, on the TF-IDF features.
5.  **Evaluation:** Assesses the model's performance on the test set using a confusion matrix and a classification report (accuracy, precision, recall).

This project covers the following key skills:
*   Natural Language Processing (NLP)
*   Text Classification
*   TF-IDF Vectorization
*   Building `scikit-learn` pipelines

## 💾 Dataset

This project includes sample datasets, `Fake.csv` and `True.csv`, located in the `data/` directory. They contain sample news articles to demonstrate the classification workflow.

**No data download is required.**

## 📁 Project Structure

```
project_11_fake_news_detection/
│
├── data/
│   ├── Fake.csv  # Sample fake news data included
│   └── True.csv  # Sample real news data included
│
├── fake_news_detection.ipynb  # Main analysis and classification notebook
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
3.  Open and run the `fake_news_detection.ipynb` notebook.
