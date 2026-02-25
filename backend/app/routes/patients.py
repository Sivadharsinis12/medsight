from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Patient
from app.schemas import PatientCreate
from app.services.risk_engine import calculate_risk

router = APIRouter()

@router.post("/")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):

    risk = calculate_risk(patient.age, patient.diagnosis)

    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        diagnosis=patient.diagnosis,
        risk_level=risk
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()