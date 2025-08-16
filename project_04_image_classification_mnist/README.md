# Project 4: Image Classification with MNIST

This project builds and trains a Convolutional Neural Network (CNN) to classify handwritten digits from the famous MNIST dataset. It serves as a foundational project for learning deep learning and computer vision.

## 📜 Description

The notebook `image_classification_mnist.ipynb` provides a step-by-step guide to:
1.  **Data Loading:** Automatically downloads and loads the MNIST dataset using TensorFlow/Keras.
2.  **Data Preprocessing:** Reshapes and normalizes the image data to prepare it for the CNN, and one-hot encodes the labels.
3.  **EDA:** Visualizes sample digits to get a feel for the dataset.
4.  **CNN Model Building:** Constructs a sequential CNN model with convolutional, pooling, and dense layers.
5.  **Model Training:** Trains the model on the MNIST training data and validates its performance.
6.  **Evaluation:** Assesses the model's accuracy using the test set and visualizes performance with a confusion matrix and classification report.

This project covers the following key skills:
*   Deep Learning for Image Classification
*   Convolutional Neural Networks (CNNs)
*   Image Preprocessing
*   Model Training and Evaluation with TensorFlow/Keras

## 💾 Dataset

The **MNIST dataset** is a large database of handwritten digits that is commonly used for training and testing in the field of machine learning. It is one of the "hello world" datasets of computer vision.

This project requires no manual data download. The dataset is fetched automatically from the `tensorflow.keras.datasets` module within the notebook.

## 📁 Project Structure

```
project_04_image_classification_mnist/
│
├── image_classification_mnist.ipynb  # Main notebook for classification
├── requirements.txt                  # Project dependencies
└── README.md                         # This file
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
3.  Open and run the `image_classification_mnist.ipynb` notebook. The notebook will automatically download the required data.
