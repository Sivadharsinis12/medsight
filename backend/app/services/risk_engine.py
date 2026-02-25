def calculate_risk(patient_data: dict):

    risk_score = 0

    if patient_data.get("age", 0) > 60:
        risk_score += 2

    if patient_data.get("blood_pressure", 0) > 140:
        risk_score += 2

    if patient_data.get("glucose", 0) > 180:
        risk_score += 2

    if risk_score >= 4:
        return "High"
    elif risk_score >= 2:
        return "Medium"
    else:
        return "Low"