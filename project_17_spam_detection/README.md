# Project 17: Spam Detection

## Objective
The objective of this project is to build a text classification model to distinguish between spam and non-spam messages. We will use the "20 Newsgroups" dataset, a classic dataset for text categorization, and treat a subset of the newsgroups as "spam" and another subset as "ham" (non-spam).

## Dataset
This project uses the **20 Newsgroups** dataset, which is available directly from the `scikit-learn` library. This dataset comprises around 18,000 newsgroup posts on 20 topics. For this project, we will select a few categories to represent "spam" and "ham".

- **Source**: `sklearn.datasets.fetch_20newsgroups`
- **Selected "Ham" Categories**: `rec.sport.baseball`, `sci.space`
- **Selected "Spam" Categories**: `talk.politics.guns`, `misc.forsale`

This approach allows us to build a spam detection model without relying on external datasets that may be difficult to access.

## Project Plan
1.  **Data Loading and Preparation**:
    -   Load the 20 Newsgroups dataset using `scikit-learn`.
    -   Select the specified categories for "spam" and "ham" to create a binary classification problem.
2.  **Text Preprocessing and Feature Extraction**:
    -   Convert the text data into numerical features using the TF-IDF (Term Frequency-Inverse Document Frequency) vectorization technique. This will transform the text into a format suitable for machine learning models.
3.  **Model Building and Training**:
    -   Split the data into training and testing sets.
    -   Implement and train a classification model, such as Multinomial Naive Bayes or a Support Vector Machine (SVM), which are well-suited for text classification tasks.
4.  **Model Evaluation**:
    -   Evaluate the model's performance using standard classification metrics, including:
        -   Accuracy
        -   Precision
        -   Recall
        -   F1-score
    -   Analyze the confusion matrix to understand the types of errors the model is making.
5.  **Conclusion**:
    -   Summarize the model's performance and discuss the effectiveness of the chosen approach for spam detection.

## Technologies
- Python
- Scikit-learn
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
