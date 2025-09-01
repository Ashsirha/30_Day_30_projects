# 30 Days, 30 Data Science Projects 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

Welcome to the **30 Days, 30 Data Science Projects** challenge!  
This repository is a comprehensive, hands-on collection of 30 data science mini-projects spanning supervised learning, unsupervised learning, time series, NLP, computer vision, recommendation systems, anomaly detection, and generative tasks. Each project is self-contained with its own Jupyter notebook, README, and `requirements.txt`, designed to build practical skills through real-world applications.

Whether you're a beginner looking to dive into data science, a job seeker building a portfolio, or an expert refining techniques, this repo offers structured learning paths, reproducible code, and insights into cutting-edge tools. Inspired by open-source communities and real datasets, it's perfect for interviews, hackathons, or personal growth.

⭐ **Star this repo** if it helps your journey! Contributions and feedback are welcome.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Tech Stack](#-tech-stack)
- [Repository Conventions](#-repository-conventions)
- [Project List & Descriptions](#-project-list--descriptions)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [Tips for Success](#-tips-for-success)
- [Coding Standards & Best Practices](#-coding-standards--best-practices)
- [Roadmap & Future Plans](#-roadmap--future-plans)
- [Common Pitfalls & Checks](#-common-pitfalls--checks)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)
- [Connect](#-connect)

---

## 🌟 Project Overview
This monorepo encapsulates a 30-day challenge to master data science fundamentals and advanced topics. Projects are organized into folders (e.g., [`project_01_titanic_survival`](project_01_titanic_survival)) and cover diverse domains like classification, regression, clustering, NLP, and deep learning. Each project includes:
- **Jupyter Notebooks**: Executable code with narratives, visualizations, and step-by-step workflows.
- **Datasets**: Sourced from public repositories (e.g., Kaggle, UCI, TensorFlow Datasets); some require manual download for licensing reasons.
- **Documentation**: Per-project READMEs with objectives, datasets, workflows, and results.
- **Shared Resources**: Root-level guidance, templates, and utilities for consistency.

Key goals:
- **Reproducibility**: Set random seeds for stochastic processes.
- **Skill-Building**: From EDA to deployment, with metrics like F1, ROC-AUC, BLEU, and ROUGE.
- **Ethics & Best Practices**: Handle imbalanced data, anonymize sensitive info, and document biases (e.g., in credit scoring or fraud detection).
- **Deployment Ready**: Export models (e.g., `.keras`, `.pkl`) and include inference snippets.

This repo is ideal for:
- Learning pipelines: Data loading → Cleaning → EDA → Modeling → Evaluation → Conclusion.
- Experimentation: Modify code, add features, or integrate new libraries.
- Portfolio Showcase: Demonstrate end-to-end projects in interviews.

---

## 🛠️ Tech Stack
- **Core Language**: Python 3.10+
- **Data Handling**: NumPy, Pandas
- **Visualization**: Matplotlib, Seaborn, Plotly (optional)
- **Machine Learning**: Scikit-learn (classification, regression, clustering)
- **Deep Learning**: TensorFlow/Keras (CNNs, LSTMs, Seq2Seq); PyTorch (planned for some projects)
- **NLP**: NLTK, SpaCy, Transformers (e.g., for summarization, sentiment)
- **Time Series**: Statsmodels, Prophet (planned), PMDARIMA
- **Computer Vision**: OpenCV, TensorFlow Datasets (e.g., MNIST, Flickr8k)
- **Other**: Jupyter Notebook for interactive development; Streamlit/FastAPI for dashboards/APIs (future extensions)
- **Environment**: Per-project `requirements.txt`; optional root `environment.yml` for Conda.

Dependencies are minimal per project to avoid bloat. Pin versions for stability.

---

## 📏 Repository Conventions
- **Folder Naming**: `project_XX_<short_snake_case_name>` (e.g., [`project_01_titanic_survival`](project_01_titanic_survival)) with zero-padded indices.
- **Per-Project Structure**:
  - `notebook.ipynb`: Main analysis file with numbered sections (1. Setup, 2. Data, etc.).
  - [`README.md`](README.md): Tailored overview, dataset details, how-to-run, results.
  - `requirements.txt`: Project-specific deps.
  - `data/`: Subfolder for datasets (download scripts if needed); avoid committing large/proprietary files.
- **Shared Guidance**: Root [`README.md`](README.md) for the full challenge; per-project docs for specifics.
- **Artifacts**: Save models, logs, plots to `artifacts/` to keep root clean.
- **Templates**: Use [`project_template`](project_template) for new projects—copy, rename, and customize.

---

## 📚 Project List & Descriptions
Below is the complete list of projects, aligned with the folder structure. Each includes a brief description, key skills, and links to relevant files. Projects are categorized by domain for easy navigation.

### Supervised Learning
1. **Titanic Survival Classification**  
   Predict passenger survival using tabular data.  
   *Skills: Binary classification, feature engineering, EDA.*  
   [Project Folder](project_01_titanic_survival) | [Notebook](project_01_titanic_survival/titanic_survival_classification.ipynb) | [README](project_01_titanic_survival/README.md)

2. **Movie Recommendation System**  
   Build collaborative filtering for movie recommendations.  
   *Skills: Similarity metrics, matrix factorization.*  
   [Project Folder](project_02_movie_recommendation) | [Notebook](project_02_movie_recommendation/movie_recommendation.ipynb) | [README](project_02_movie_recommendation/README.md)

3. **Stock Price Prediction**  
   Forecast stock trends using ARIMA and LSTM.  
   *Skills: Time series, ARIMA, LSTMs.*  
   [Project Folder](project_03_stock_price_prediction) | [Notebook](project_03_stock_price_prediction/stock_price_prediction.ipynb) | [README](project_03_stock_price_prediction/README.md)

4. **Image Classification with MNIST**  
   Classify handwritten digits.  
   *Skills: CNNs, augmentation, callbacks.*  
   [Project Folder](project_04_image_classification_mnist) | [Notebook](project_04_image_classification_mnist/image_classification_mnist.ipynb) | [README](project_04_image_classification_mnist/README.md)

5. **Sentiment Analysis on Twitter Data**  
   Classify tweet polarity.  
   *Skills: NLP, word embeddings, LSTMs.*  
   [Project Folder](project_05_sentiment_analysis_twitter) | [Notebook](project_05_sentiment_analysis_twitter/sentiment_analysis_twitter.ipynb) | [README](project_05_sentiment_analysis_twitter/README.md)

6. **Customer Segmentation**  
   Group mall customers by behavior.  
   *Skills: K-Means, Elbow method, visualization.*  
   [Project Folder](project_06_customer_segmentation) | [Notebook](project_06_customer_segmentation/customer_segmentation.ipynb) | [README](project_06_customer_segmentation/README.md)

7. **House Price Prediction**  
   Estimate property values.  
   *Skills: Regression, feature engineering, XGBoost.*  
   [Project Folder](project_07_house_price_prediction) | [Notebook](project_07_house_price_prediction/house_price_prediction.ipynb) | [README](project_07_house_price_prediction/README.md)

8. **Credit Card Fraud Detection**  
   Detect fraudulent transactions.  
   *Skills: Imbalanced data, undersampling, PR-AUC.*  
   [Project Folder](project_08_credit_card_fraud_detection) | [Notebook](project_08_credit_card_fraud_detection/credit_card_fraud.ipynb) | [README](project_08_credit_card_fraud_detection/README.md)

9. **World Happiness Report EDA**  
   Analyze global happiness factors.  
   *Skills: EDA, correlation, regional analysis.*  
   [Project Folder](project_09_world_happiness_report_eda) | [Notebook](project_09_world_happiness_report_eda/world_happiness_eda.ipynb) | [README](project_09_world_happiness_report_eda/README.md)

10. **COVID-19 Time Series**  
    Analyze pandemic trends.  
    *Skills: Time series, visualization, forecasting.*  
    [Project Folder](project_10_covid19_time_series) | [Notebook](project_10_covid19_time_series/covid19_time_series.ipynb) | [README](project_10_covid19_time_series/README.md)

11. **Fake News Detection**  
    Detect veracity in news articles.  
    *Skills: NLP, supervised learning, pipelines.*  
    [Project Folder](project_11_fake_news_detection) | [Notebook](project_11_fake_news_detection/fake_news_detection.ipynb) | [README](project_11_fake_news_detection/README.md)

12. **Air Quality Prediction**  
    Forecast pollutant levels.  
    *Skills: Regression, temporal modeling, feature engineering.*  
    [Project Folder](project_12_air_quality_prediction) | [Notebook](project_12_air_quality_prediction/air_quality_prediction.ipynb) | [README](project_12_air_quality_prediction/README.md)

13. **Heart Disease Prediction**  
    Classify heart disease risk from medical attributes.  
    *Skills: Classification, medical data, ROC curves.*  
    [Project Folder](project_13_heart_disease_prediction) | [Notebook](project_13_heart_disease_prediction/heart_disease_prediction.ipynb) | [README](project_13_heart_disease_prediction/README.md)

14. **Customer Churn Prediction**  
    Predict bank customer churn.  
    *Skills: Classification, imbalance handling, PR curves.*  
    [Project Folder](project_14_customer_churn_prediction) | [Notebook](project_14_customer_churn_prediction/customer_churn_prediction.ipynb) | [README](project_14_customer_churn_prediction/README.md)

15. **Sales Prediction**  
    Predict retail sales.  
    *Skills: Regression, time series, MAE/RMSE.*  
    [Project Folder](project_15_sales_prediction) | [Notebook](project_15_sales_prediction/sales_prediction.ipynb) | [README](project_15_sales_prediction/README.md)

16. **Employee Attrition Prediction**  
    Forecast HR attrition risks.  
    *Skills: Classification, feature selection, ethics.*  
    [Project Folder](project_16_employee_attrition_prediction) | [Notebook](project_16_employee_attrition_prediction/employee_attrition_prediction.ipynb) | [README](project_16_employee_attrition_prediction/README.md)

17. **Spam Detection**  
    Classify emails as spam/ham.  
    *Skills: NLP, TF-IDF, text classification.*  
    [Project Folder](project_17_spam_detection) | [Notebook](project_17_spam_detection/spam_detection.ipynb) | [README](project_17_spam_detection/README.md)

18. **Credit Scoring**  
    Assess loan default probability.  
    *Skills: Classification, fairness, ROC-AUC.*  
    [Project Folder](project_18_credit_scoring) | [Notebook](project_18_credit_scoring/credit_scoring.ipynb) | [README](project_18_credit_scoring/README.md)

19. **Time Series Forecasting**  
    Generic forecasting framework.  
    *Skills: ARIMA, SARIMAX, stationarity tests.*  
    [Project Folder](project_19_time_series_forecasting) | [Notebook](project_19_time_series_forecasting/time_series_forecasting.ipynb) | [README](project_19_time_series_forecasting/README.md)

20. **Sentiment Analysis Movie Reviews**  
    Analyze IMDb reviews.  
    *Skills: NLP, embeddings, binary classification.*  
    [Project Folder](project_20_sentiment_analysis_movie_reviews) | [Notebook](project_20_sentiment_analysis_movie_reviews/sentiment_analysis_movie_reviews.ipynb) | [README](project_20_sentiment_analysis_movie_reviews/README.md)

21. **Image Captioning**  
    Generate captions from images.  
    *Skills: CV + NLP, Seq2Seq, BLEU.*  
    [Project Folder](project_21_image_captioning) | [Notebook](project_21_image_captioning/image_captioning.ipynb) | [README](project_21_image_captioning/README.md)

22. **Recommender System**  
    Embeddings-based recommendations.  
    *Skills: Collaborative filtering, embeddings, ranking.*  
    [Project Folder](project_22_recommender_system) | [Notebook](project_22_recommender_system/recommender_system.ipynb) | [README](project_22_recommender_system/README.md)

23. **Advanced Credit Card Fraud Detection**  
    Detect fraudulent transactions (advanced).  
    *Skills: SMOTE, class weights, confusion matrix.*  
    [Project Folder](project_23_credit_card_fraud_detection) | [Notebook](project_23_credit_card_fraud_detection/credit_card_fraud_detection.ipynb) | [README](project_23_credit_card_fraud_detection/README.md)

24. **Customer Segmentation for Retail**  
    RFM-based clustering for retail.  
    *Skills: RFM analysis, K-Means, segmentation.*  
    [Project Folder](project_24_customer_segmentation_retail) | [Notebook](project_24_customer_segmentation_retail/customer_segmentation_retail.ipynb) | [README](project_24_customer_segmentation_retail/README.md)

25. **Text Summarization**  
    Generate article summaries.  
    *Skills: Seq2Seq, attention, ROUGE.*  
    [Project Folder](project_25_text_summarization) | [Notebook](project_25_text_summarization/text_summarization.ipynb) | [README](project_25_text_summarization/README.md)

26. **Machine Translation**  
    Neural machine translation.  
    *Skills: Transformers, Seq2Seq, BLEU.*  
    [Project Folder](project_26_machine_translation) | [Notebook](project_26_machine_translation/machine_translation.ipynb) | [README](project_26_machine_translation/README.md)

27. **Object Detection**  
    Detect objects in images.  
    *Skills: CNNs, YOLO/SSD, mAP.*  
    [Project Folder](project_27_object_detection) | [Notebook](project_27_object_detection/object_detection.ipynb) | [README](project_27_object_detection/README.md)

28. **Predictive Maintenance**  
    Predict machine failures.  
    *Skills: Classification, sensor data, RUL.*  
    [Project Folder](project_28_predictive_maintenance) | [Notebook](project_28_predictive_maintenance/predictive_maintenance.ipynb) | [README](project_28_predictive_maintenance/README.md)

29. **Anomaly Detection**  
    Unsupervised outlier detection.  
    *Skills: Isolation Forest, scoring, visualization.*  
    [Project Folder](project_29_anomaly_detection) | [Notebook](project_29_anomaly_detection/anomaly_detection.ipynb) | [README](project_29_anomaly_detection/README.md)

*Note: Some projects (e.g., 26) are placeholders. Check [`PROJECT_INDEX.md`](PROJECT_INDEX.md) for status.*

---

## 🗂️ Repository Structure
```
30_Day_30_projects/
├── README.md                          # This file (root overview)
├── PROJECT_INDEX.md                   # Live project status & tasks
├── LICENSE                            # MIT License
├── requirements.txt                   # Core dependencies
├── .github/                           # GitHub configs (e.g., copilot instructions)
├── project_01_titanic_survival/       # Example project folder
│   ├── titanic_survival_classification.ipynb
│   ├── README.md
│   ├── requirements.txt
│   └── data/                          # Datasets (if included)
├── project_02_movie_recommendation/   # Another project
│   └── ...
├── project_template/                  # Template for new projects
└── ...                                # Up to project_30
```

---

## 🚀 Getting Started
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ashsirha/30_Day_30_projects.git
   cd 30_Day_30_projects
   ```

2. **Set Up Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
   For project-specific deps: `pip install -r project_XX/requirements.txt`.

3. **Download Datasets**: Many projects require manual downloads (e.g., from Kaggle). Follow per-project READMEs.

4. **Run a Notebook**:
   ```bash
   jupyter notebook
   ```
   Open any `project_XX/notebook.ipynb` and run cells top-to-bottom.

5. **Experiment**: Modify code, add models, or visualize results.

---

## 💡 Tips for Success
- **Start Simple**: Begin with EDA-focused projects like Titanic or Happiness EDA.
- **Reproduce First**: Run notebooks as-is to understand workflows.
- **Experiment Freely**: Add callbacks (EarlyStopping), try SMOTE for imbalance, or integrate PyTorch.
- **Metrics Matter**: Use appropriate metrics (e.g., F1 for imbalance, BLEU for generation).
- **Version Control**: Branch for changes (e.g., `feat/add-pytorch`).
- **Interview Prep**: Discuss trade-offs (e.g., ARIMA vs. LSTM for forecasting).
- **Avoid Pitfalls**: Always split data (train/val/test), set seeds, and document assumptions.

---

## 📝 Coding Standards & Best Practices
- **Reproducibility**: Set seeds (NumPy, random, TensorFlow) for stochastic tasks.
- **Notebooks**: Structured sections with headings; encapsulate logic in functions.
- **Error Handling**: Use try-except for data loading; validate inputs.
- **Security**: Anonymize PII; avoid committing sensitive data.
- **Performance**: Vectorize ops; use batching/GPU for DL.
- **Documentation**: Comment code; update READMEs with results.
- **Testing**: Light unit tests for utilities (future addition).
- **Deployment**: Export models; add inference scripts.

---

## 🗺️ Roadmap & Future Plans
- [ ] Standardize all READMEs with consistent structure.
- [ ] Add root `environment.yml` for unified Conda setup.
- [ ] Introduce CI (GitHub Actions) for notebook smoke tests.
- [ ] Integrate model cards for sensitive domains (e.g., health, finance).
- [ ] Expand to 35+ projects (e.g., more generative AI).
- [ ] Add lightweight test suite for shared utilities.
- [ ] Dashboard extensions with Streamlit/FastAPI.

Track progress in [`PROJECT_INDEX.md`](PROJECT_INDEX.md).

---

## ⚠️ Common Pitfalls & Checks
- **Data Splits**: Never forget validation/test separation.
- **Imbalance**: Report ROC-AUC/PR-AUC, not just accuracy.
- **Seeds**: Non-reproducible results without seeding.
- **Large Files**: Use `data/` subfolders; avoid embedding in notebooks.
- **Ethics**: Document biases in credit/fraud projects.
- **Overfitting**: Use callbacks; monitor val loss.

---

## 🤝 Contributing
We love contributions! Here's how:
1. Fork the repo.
2. Create a branch: `git checkout -b feat/your-feature`.
3. Make changes: Add projects, fix bugs, improve docs.
4. Test: Ensure notebooks run clean.
5. Commit: `git commit -m "Add: New project on X"`.
6. PR: Open a pull request with details.

Guidelines:
- Follow conventions (e.g., folder naming).
- Update [`PROJECT_INDEX.md`](PROJECT_INDEX.md) for new tasks.
- Suggest projects via issues.

---

## 📄 License
This project is licensed under the MIT License. See the file for details.

---

## 🙏 Acknowledgements
- **Datasets**: Kaggle, UCI ML Repository, TensorFlow Datasets, open government portals.
- **Inspiration**: Open-source DS communities, portfolios, and challenges.
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, TensorFlow, PyTorch, NLTK, SpaCy, Plotly, Streamlit.
- **Community**: Thanks to contributors and users for feedback!

---

## 🌟 Connect
- **GitHub**: [Ashsirha](https://github.com/Ashsirha)

Found this helpful? ⭐ Star the repo and share! Questions? Open an issue.

Happy coding! 🚀

---
*✨ Ash & AI: 2025-08-31 12:00 ET*
