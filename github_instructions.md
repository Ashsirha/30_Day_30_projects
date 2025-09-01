# Repository Working Instructions

## Purpose
Provide a consistent process for adding, improving, and reviewing the 30 mini data science & ML projects. Acts as a living contributor guide + task tracker.

## Quick Start
- Pick a project folder: `project_XX_<name>`
- Create/activate a virtual environment
- `pip install -r requirements.txt`
- Run notebook top-to-bottom; ensure no errors
- Save artifacts (models/logs) in an `artifacts/` subfolder (create if missing)

## Project Standard Template
Each project README should include:
1. Title & One-line summary
2. Objective / Problem Statement
3. Dataset (source, description, retrieval steps, license notes)
4. Project Structure tree
5. Methodology / Workflow steps
6. Key Techniques / Algorithms
7. How to Run (env + commands)
8. Results (metrics, sample outputs) – update after training
9. Possible Improvements / Next Steps
10. References / Acknowledgements

## Notebook Section Headings
1. Setup & Imports
2. Data Loading
3. Data Understanding & EDA
4. Preprocessing / Feature Engineering
5. Modeling / Training
6. Evaluation & Error Analysis
7. (Optional) Deployment / Inference Demo
8. Conclusions & Future Work

## Quality Checklist (Per Project)
- [ ] README present and follows template
- [ ] Dataset instructions reproducible
- [ ] Seeds set for reproducibility (random, numpy, framework)
- [ ] Clear separation of train/validation/test
- [ ] Appropriate metrics (classification: accuracy + F1/ROC-AUC; regression: MAE/RMSE; clustering: silhouette where applicable)
- [ ] Visualization of key insights
- [ ] Error analysis (e.g., misclassified, top residuals) where meaningful
- [ ] Model artifacts saved (if training cost > a few seconds)
- [ ] Dependencies minimal & pinned if instability observed
- [ ] No large raw datasets committed (only small samples if needed)

## Cross-Project Tasks
- [ ] Align root README ordering with actual folder list
- [ ] Eliminate or rename duplicate domain folders (e.g., second fraud detection project)
- [ ] Add unified environment file (optional)
- [ ] Create automation script to regenerate index table
- [ ] Introduce CI to smoke test critical notebooks (reduced epochs)
- [ ] Add LICENSE/usage note to each domain touching sensitive data (health, finance)

## Task Tracker
| ID | Task | Status | Notes |
|----|------|--------|-------|
| 1 | Standardize placeholder READMEs (16–29) | Pending | Use template | 
| 2 | Reconcile root README list vs actual folders | Pending | Requires mapping table |
| 3 | Add artifact subfolders for trained models | In Progress | Some models saved in root |
| 4 | Add CI notebook smoke test | Pending | GitHub Actions |
| 5 | Add model cards for sensitive projects | Pending | Fraud / Credit / Health |
| 6 | Create unified requirements or env file | Pending | Evaluate duplicates |

## Review Process
1. Open PR referencing task tracker ID(s).
2. In PR description: summarize changes + before/after metrics (if model updated).
3. Verify all modified notebooks run clean via `Restart & Run All`.
4. Reviewer checks checklist compliance before merge.

## Versioning & Branching
- Feature branches: `feat/<short-desc>`
- Fix branches: `fix/<issue>`
- Documentation: `docs/<scope>`

## Security & Compliance
- Do not commit API keys / credentials.
- For Kaggle downloads, require users to authenticate locally; never embed secrets.
- Respect dataset licenses; link instead of embedding restricted data.

## Performance Tips
- Use vectorized ops; avoid loops through DataFrame rows.
- For deep learning: enable mixed precision if GPU available (`tf.keras.mixed_precision.set_global_policy('mixed_float16')`) where beneficial.

## Future Improvements Backlog
- [ ] Add evaluation dashboard notebook aggregator
- [ ] Introduce poetry/uv for dependency management
- [ ] Convert repeated code into shared `common/` utilities module
- [ ] Add black + flake8 pre-commit hooks
- [ ] Provide dataset download scripts (`scripts/get_data_<project>.py`)

---
*✨ AI-crafted on 2025-08-31*
