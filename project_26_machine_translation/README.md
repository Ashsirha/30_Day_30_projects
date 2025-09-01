# Project 26: Machine Translation

## Objective
Build a neural machine translation (NMT) model to translate sentences from a source language (e.g., English) to a target language (e.g., German). Demonstrates sequence-to-sequence modeling with attention or Transformer architectures.

## Dataset
Recommended datasets:
- WMT14 En-De (subset) – large, may need sampling
- Multi30k (smaller, good for fast experimentation)

Obtain data via `torchtext`, `datasets` (Hugging Face), or `tensorflow_datasets` and store in `data/`.

## Workflow
1. Data acquisition & cleaning (tokenization, lowercasing, optional subword/BPE)
2. Vocabulary / tokenizer build (SentencePiece or WordPiece)
3. Train/val/test split (ensure no leakage)
4. Baseline seq2seq w/ attention (LSTM) OR Transformer encoder-decoder
5. Training with teacher forcing / label smoothing
6. Evaluation: BLEU, SacreBLEU, length ratio, example translations
7. Inference beam search vs greedy comparison
8. Error analysis: unknown tokens, hallucinations
9. Optional: Fine-tune pre-trained Marian / mBART / T5

## Metrics
- SacreBLEU (primary)
- Tokenized BLEU, chrF (secondary)
- Inference latency (ms/sentence) – optional

## How to Run
```bash
pip install -r requirements.txt
jupyter notebook
```

## Improvements
- Add scaling laws (dataset size vs BLEU)
- Mixed precision + gradient accumulation for larger batches
- Back-translation for data augmentation

## Ethics & Considerations
Translation quality may vary by dialect or domain. Avoid misuse in safety-critical contexts without human review.

---
*Created 2025-08-31*
