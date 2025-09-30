# Project 26: Machine Translation

## Objective
The objective of this project is to build a neural machine translation model that can translate text from one language to another. We will use a sequence-to-sequence (Seq2Seq) model with attention mechanism to translate between French and English.

## Dataset
This project uses the **French-English Translation dataset**, which contains paired sentences in French and English for training the translation model.

- **Source**: Tab-delimited Bilingual Sentence Pairs from the Tatoeba Project
- **Data File**: `fra-eng.zip` (included in this directory)
- **Format**: Each line contains an English sentence followed by a tab and its French translation

### Dataset Details:
The dataset contains thousands of sentence pairs that will be used to train the neural machine translation model. The sentences cover various topics and complexity levels, making it suitable for learning translation patterns.

## Project Plan
1. **Data Loading and Preparation**:
   - Extract and load the French-English sentence pairs from the zip file.
   - Preprocess the text data by cleaning, tokenizing, and creating vocabularies for both languages.
   - Split the data into training and validation sets.

2. **Text Preprocessing**:
   - Clean the text data (remove special characters, normalize case).
   - Tokenize sentences and create word-to-index mappings.
   - Add start-of-sequence and end-of-sequence tokens.
   - Pad sequences to uniform length.

3. **Model Building**:
   - Build a Seq2Seq model with encoder-decoder architecture using LSTMs or GRUs.
   - Implement an attention mechanism to help the model focus on relevant parts of the source sentence.
   - Design the architecture to handle variable-length sequences.

4. **Model Training**:
   - Train the model on the preprocessed sentence pairs.
   - Use teacher forcing during training to improve convergence.
   - Monitor training progress with validation loss.

5. **Translation and Evaluation**:
   - Implement inference functions to translate new sentences.
   - Use beam search or greedy search for generating translations.
   - Evaluate translation quality using BLEU score metrics.

6. **Conclusion**:
   - Summarize the model's performance and showcase translation examples.
   - Discuss potential improvements and applications.

## Technologies
- Python
- TensorFlow/Keras
- NumPy
- Matplotlib
- Jupyter Notebook
- NLTK (for BLEU score evaluation)
- Regular Expressions (for text preprocessing)