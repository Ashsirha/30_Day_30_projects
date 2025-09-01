# Copilot Project Instructions

## Project Overview
A monorepo of 30 (implemented + planned) data science & machine learning mini-projects spanning supervised learning, unsupervised learning, time series, NLP, computer vision, recommendation, anomaly detection, and generative tasks. Each project folder is self-contained with its own notebook, README, and per-project `requirements.txt`.

## Tech Stack
- Python 3.10+
- Core libs: numpy, pandas, scikit-learn, matplotlib, seaborn
- Deep learning: TensorFlow/Keras (some future projects may add PyTorch)
- NLP: nltk, spacy, transformers (planned in later projects)
- Time series: statsmodels, prophet (planned), pmdarima (optional)
- Visualization: matplotlib, seaborn, plotly (optional), streamlit (for dashboards)

## Repository Conventions
- Folder naming: `project_XX_<short_snake_case_name>` (2-digit zero-padded index)
- Each project: `README.md`, main notebook, `requirements.txt`, optional `data/` subfolder
- Shared guidance: root `README.md` describes the full challenge; per-project README tailored to that domain.
- Experimental artifacts: prefer saving into a `artifacts/` subfolder (models, logs) to keep root clean.

## Coding Standards
- Reproducibility: set random seeds (numpy, random, tensorflow) where stochastic training occurs.
- Notebooks: top-level narrative sections with numbered headings (1. Setup, 2. Data, 3. EDA, 4. Modeling, 5. Evaluation, 6. Conclusion)
- Functions: encapsulate repetitive preprocessing/model evaluation logic in helper functions within notebook or a lightweight `utils.py` (if reuse across multiple cells).
- Metrics: choose metrics appropriate to task (e.g., F1/ROC-AUC for imbalance, MAE/RMSE for regression, BLEU/ROUGE for translation/summarization).

## Patterns & Utilities
- Validation split: always reserve legit test set; optionally stratify classification tasks.
- Callbacks (DL): EarlyStopping, ReduceLROnPlateau, ModelCheckpoint.
- Imbalanced data: show class distribution, apply resampling (SMOTE, class weights) and report confusion matrix + PR curve.
- Error analysis: list common misclassifications or residual plots (regression).

## Testing Strategy
- Light unit tests (if added scripts) under `tests/` (future improvement) verifying utility functions (e.g., preprocessing does not change label counts unexpectedly).
- For now, notebooks serve as executable documentation; ensure they run top-to-bottom without manual intervention.

## Deployment & Reuse
- Export trained model (e.g., `.keras` / `.pkl`) + small inference snippet in README for applied projects.
- For dashboard or API oriented extensions, use Streamlit or FastAPI (future step) inside a new `app/` subfolder.

## Environment Management
- Per-project `requirements.txt` should remain minimal; pin major versions if incompatibilities arise.
- Optionally create a root `environment.yml` for unified conda environment (pending).

## Security & Data Ethics
- Avoid committing proprietary or licensed third-party datasets; use download scripts or instructions.
- For PII-like datasets (none currently), document anonymization steps.

## Performance Guidelines
- Prefer vectorized numpy/pandas ops; avoid Python loops over rows.
- Use batching and GPU acceleration for deep learning; limit epochs with callbacks to prevent overfitting.

## Contribution Workflow
1. Branch from `main` using descriptive name: `feat/mnist-augmentation`, `fix/readme-alignment`.
2. Ensure linting (flake8/black optional future addition) & notebooks run clean.
3. Update project README if changing approach/results.
4. Open PR with concise summary + before/after metrics.

## Adding a New Project
1. Copy `project_template/` to `project_XX_new_topic` with next number.
2. Fill in README template (overview, dataset, objective, workflow, how to run, results placeholder).
3. Implement notebook with structured sections + TODO markers for future enhancements.
4. Update root README index (future automation script can parse).

## Roadmap (High-Level)
- [ ] Standardize remaining placeholder READMEs with consistent structure.
- [ ] Add unified environment spec.
- [ ] Introduce lightweight test suite for shared utilities.
- [ ] Integrate CI (GitHub Actions) to execute a smoke test on a subset of notebooks (e.g., fast mode with fewer epochs).
- [ ] Add model cards for sensitive domains (fraud, credit scoring, health).

## Common Pitfalls & Checks
- Forgetting to separate validation from test – always verify.
- Reporting only accuracy on imbalanced sets – add ROC-AUC & PR-AUC.
- Skipping seed setting – leads to non-reproducible results.
- Oversized notebooks due to embedded large data – prefer external data folder.

## Glossary
- EDA: Exploratory Data Analysis
- SMOTE: Synthetic Minority Over-sampling Technique
- ROC-AUC: Area Under Receiver Operating Characteristic Curve

---
*✨ Crafted collaboratively by **Ash** & **AI (GitHub Copilot)** — 2025-08-31 00:00 New York Time (EDT) · 2025-08-31 04:00 UTC*

<!-- 🤖 Timestamp: Generated in America/New_York (EDT), with UTC reference for reproducibility. -->
