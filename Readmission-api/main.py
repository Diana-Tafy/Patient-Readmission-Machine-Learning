from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Allow Lovable frontend to call this endpoint
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your exported Databricks pipeline
model = joblib.load("readmission_pipeline.pkl")

from pydantic import BaseModel, Field

class PatientData(BaseModel):
    age: float
    length_of_stay: float
    blood_sugar_levels: float
    number_of_diagnoses: float
    gender: Field(..., example="Female")

@app.post("/predict")
def predict_readmission(patient: PatientData):
    # Match the exact feature names your trained model expects
    input_df = pd.DataFrame([{
        'Age': patient.age,
        'Length of Stay': patient.length_of_stay,
        'Blood Sugar Levels': patient.blood_sugar_levels,
        'Number of Diagnoses': patient.number_of_diagnoses,
        'Gender': patient.gender
    }])
    
    # Get prediction probability
    prob = float(model.predict_proba(input_df)[0][1])
    
    if prob >= 0.5:
        status = "High Risk"
    elif prob >= 0.3:
        status = "Moderate Risk"
    else:
        status = "Low Risk"
        
    return {
        "status": status,
        "probability": round(prob * 100, 1)
    }