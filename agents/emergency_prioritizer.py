class EmergencyPrioritizer:
    def score(self, hazard_type, severity, description, threats, resources):
        score = 50
        if severity == "high":
            score += 50
        if hazard_type == "medical":
            score += 20
        level = "CRITICAL" if score >= 90 else "HIGH" if score >= 70 else "MEDIUM"
        return {"priority_score": score, "priority_level": level}
