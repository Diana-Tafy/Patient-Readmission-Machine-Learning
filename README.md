# Patient-Readmission-Machine-Learning
ML Model 

# 🏥 Patient Readmission Risk Prediction API

An end-to-end Healthcare Analytics solution featuring a machine learning classification pipeline trained on patient data and deployed as a live REST API using **FastAPI** on **Render**.

---

## 📌 Project Overview
Hospital readmissions within 30 days are a critical metric for healthcare providers. This project utilizes machine learning to predict patient readmission risk, empowering clinical teams with data-driven insights to prioritize high-risk care management and post-discharge interventions.

---

## 🚀 Live Links
* **Live API Base URL:** [https://patient-readmission-machine-learning.onrender.com](https://patient-readmission-machine-learning.onrender.com)
* **Interactive API Documentation (Swagger UI):** [https://patient-readmission-machine-learning.onrender.com/docs](https://patient-readmission-machine-learning.onrender.com/docs)
* **Frontend Web Dashboard:** *(https://patientreadmissionmodel.lovable.app)*

---

## 🛠️ Tech Stack & Tools
* **Data Processing & Pipeline:** Scikit-Learn (`ColumnTransformer`, `StandardScaler`, `OneHotEncoder`), Pandas, NumPy
* **Backend Framework:** FastAPI, Uvicorn
* **Model Serialization:** Joblib
* **Deployment Platform:** Render (Cloud Web Service)
* **Language & Versioning:** Python 3.14 (Scikit-Learn `1.6.1`)

---

## 📊 Model Input Features & Risk Logic

### Input Schema
The API accepts structured JSON payloads with the following patient metrics:

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `age` | Integer | Patient age in years |
| `length_of_stay` | Integer | Hospital stay duration (days) |
| `blood_sugar_levels` | Float/Int | Fasting or average blood glucose level (mg/dL) |
| `number_of_diagnoses` | Integer | Total recorded medical conditions |
| `gender` | String | `"Male"` or `"Female"` |

### Risk Thresholds
The model outputs a probability score (%) mapped to three clinical risk tiers:
* 🔴 **High Risk ($\ge$ 50%):** Immediate care management plan & mandatory 48-hour follow-up.
* 🟡 **Moderate Risk (30% – 49%):** Standard discharge monitoring & post-care outreach.
* 🟢 **Low Risk (< 30%):** Routine follow-up scheduled.

---

## ⚡ API Endpoint Reference

### Request (`POST /predict`)
```json
{
  "age": 68,
  "length_of_stay": 7,
  "blood_sugar_levels": 185.5,
  "number_of_diagnoses": 5,
  "gender": "Female"
}

Response Example
{
  "readmission_risk_score": 0.62,
  "risk_category": "High Risk",
  "recommendation": "Priority clinical follow-up within 48 hours."
}

Repository Structure
Patient-Readmission-Machine-Learning/
│
└── Readmission-api/
    ├── main.py                    # FastAPI application & route definitions
    ├── readmission_pipeline.pkl   # Serialized Scikit-Learn ML pipeline
    ├── requirements.txt           # Dependency management (pinned versions)
    └── README.md                  # Project documentation

Here is a concise summary of the end-to-end Data Analytics & Machine Learning solution you built:

---

## 🚀 Patient Readmission Risk Intelligence

* **Data Engineering & Lakehouse:** Ingested and prepared patient healthcare records using **SQL** and **Python** within **Databricks** to analyze key clinical risk drivers.

* **Predictive Modeling:** Trained and exported a Machine Learning classification pipeline (`readmission_pipeline.pkl`) that evaluates patient attributes (age, length of stay, blood sugar levels, diagnosis count, gender) to compute a 30-day readmission probability.

* **REST API Development:** Developed a **FastAPI** backend with explicit **Pydantic** data validation and dynamic OpenAPI/Swagger documentation, version-controlled on **GitHub**.

* **Cloud Deployment:** Configured automated CI/CD pipelines to host the live backend API on **Render**.

* **Interactive Business Dashboard:** Built a full-stack interactive web application deployed on **Lovable** that communicates directly with your API—displaying real-time risk scores (High, Moderate, Low) and actionable clinical care recommendations.
