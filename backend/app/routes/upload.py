from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os
from app.services.nlp_service import analyze_text

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_record(
    file: UploadFile = File(...),
    patient_id: str = Form(...),
    category: str = Form(default="General"),
    department: str = Form(default="General")
):
    # Save the uploaded file
    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Perform analysis on the file
    analysis = analyze_text(f"Clinical note for patient {patient_id}, category: {category}, department: {department}")

    # Determine risk level based on category
    risk_level = "Low"
    if category == "Radiology":
        risk_level = "High"
    elif category == "Lab Report":
        risk_level = "Medium"

    # Generate summary and recommendation
    summary = f"Analysis complete for {patient_id}. Category: {category}, Department: {department}."
    recommendation = "Continue regular monitoring."
    if risk_level == "High":
        recommendation = "Immediate follow-up recommended. Review imaging results."
    elif risk_level == "Medium":
        recommendation = "Schedule follow-up within 1 week."

    return {
        "patient_id": patient_id,
        "filename": file.filename,
        "category": category,
        "department": department,
        "analysis": {
            "summary": summary,
            "recommendation": recommendation,
            "risk_level": risk_level,
            "entities": analysis.get("entities", []),
            "classification": analysis.get("classification", [])
        }
    }
