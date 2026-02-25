from fastapi import APIRouter
from app.services.recommendation_engine import generate_recommendation

router = APIRouter()

@router.post("/recommendation")
def get_recommendation(data: dict):

    risk_level = data.get("risk_level")
    recommendation = generate_recommendation(risk_level)

    return {
        "risk_level": risk_level,
        "recommendation": recommendation,
        "confidence": "94%"
    }