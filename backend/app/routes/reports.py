from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_reports():
    return {
        "reports": [
            {"title": "Patient Risk Analysis Report"},
            {"title": "Diagnostic Trend Report"},
            {"title": "Quarterly Clinical Summary"}
        ]
    }