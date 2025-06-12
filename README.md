---

# 📰 Fake News Detector 🧠🚀

An end-to-end **Fake News Detection** system built using **Transformers (DistilBERT)** and **FastAPI**, wrapped in an **MLOps-style architecture** with modular components for ingestion, transformation, model training, evaluation, and serving.

---

## 🚧 Project Structure (Pipeline Stages)

```bash
📦 Fake-News-Detector/
├── app.py                         # FastAPI app for prediction and training
├── main.py                        # Pipeline trigger (manual run)
├── setup.py                       # For local package install
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker config (if deploying)
├── template.py                    # Project template automation
├── README.md                      # Project documentation
├── LICENSE                        # Open source license
├── config/
│   └── config.yaml                # Central config for paths, etc.
├── params.yaml                    # ML model training hyperparameters
├── artifact/                      # Stores pipeline outputs
│   ├── data_ingestion/
│   ├── data_transformation/
│   ├── model_trainer/
│   └── model_evalution/
├── log/
│   └── looping.log                # Logging output file
├── research/                      # Jupyter notebooks for dev and EDA
│   ├── data_ingestion.ipynb
│   ├── data_transformation.ipynb
│   ├── model_trainer.ipynb
│   ├── model_evalution.ipynb
│   ├── FakeNewsDetector.ipynb
├── src/                           # Source code
│   ├── __init__.py
│   ├── components/                # Core logic for each stage
│   ├── config/                    # Configuration manager
│   ├── constants/                 # Constants used across project
│   ├── entity/                    # Config/data entity classes
│   ├── logging/                   # Custom logging setup
│   ├── pipeline/                  # Pipeline stage execution scripts
│   └── utils/                     # Utility functions

```

---

## 🔄 Pipeline Overview

| Stage                 | Status    | Description                              |
| --------------------- | --------- | ---------------------------------------- |
| ✅ Data Ingestion      | Completed | Downloads dataset from Kaggle            |
| ✅ Data Transformation | Completed | Cleans & prepares text for model         |
| ✅ Model Training      | Completed | Fine-tunes DistilBERT on fake/real news  |
| ✅ Model Evaluation    | Completed | Predicts, logs confidence + saves to CSV |
| ✅ FastAPI Backend     | Completed | Offers `/train` and `/predict` endpoints |

---

## 🚀 FastAPI Endpoints

* **GET** `/train`
  Triggers full training pipeline
* **POST** `/predict?text=your_news_here`
  Returns predicted label (`Real News` / `Fake News`) and confidence

---

## 📦 Model Details

* **Model:** `distilbert-base-uncased`
* **Task:** Binary Text Classification
* **Framework:** HuggingFace Transformers + PyTorch
* **Storage:** Local file-based (`local_files_only=True`)

---

## 🧪 Sample Prediction Output

```
📰 Text: India successfully lands Chandrayaan-3 near the Moon's south pole
📢 Prediction: Real News (1.0000 confidence)
```

---

## 🛠 Future Improvements

* Integrate MongoDB for logging predictions
* Dockerize app for deployment
* CI/CD with GitHub Actions
* Streamlit or React frontend
* Add more pretrained models (RoBERTa, BERT, etc.)

---

## ✍️ Author

**Ayush Vishwakarma**
Machine Learning Developer | MLOps & NLP Enthusiast
📧 [ayushaiml14@gmail.com](mailto:ayushaiml14@gmail.com)

---