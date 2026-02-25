def generate_recommendation(risk_level: str):

    if risk_level == "High":
        return "Immediate specialist referral required."
    elif risk_level == "Medium":
        return "Schedule follow-up within 30 days."
    else:
        return "Continue routine monitoring."