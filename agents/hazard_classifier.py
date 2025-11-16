class HazardClassifier:
    def classify(self, description):
        description = description.lower()
        severity = "moderate"
        hazard_type = "unknown"
        triggered_keywords = []

        # Medical emergencies
        medical_keywords = ["asthma", "chest pain", "breathing", "heart attack", "unconscious", "injury", "bleeding"]
        flood_keywords = ["water", "flood", "rising", "heavy rain", "overflow"]
        fire_keywords = ["fire", "smoke", "burning", "flames", "heat"]
        earthquake_keywords = ["earthquake", "tremor", "shaking", "quake"]
        storm_keywords = ["storm", "wind", "cyclone", "hail", "thunder"]
        accident_keywords = ["accident", "collision", "vehicle", "injury"]

        if any(k in description for k in medical_keywords):
            hazard_type = "medical"
            severity = "high"
            triggered_keywords = [k for k in medical_keywords if k in description]

        elif any(k in description for k in flood_keywords):
            hazard_type = "flood"
            severity = "high" if "rising" in description or "flood" in description else "moderate"
            triggered_keywords = [k for k in flood_keywords if k in description]

        elif any(k in description for k in fire_keywords):
            hazard_type = "fire"
            severity = "high"
            triggered_keywords = [k for k in fire_keywords if k in description]

        elif any(k in description for k in earthquake_keywords):
            hazard_type = "earthquake"
            severity = "high"
            triggered_keywords = [k for k in earthquake_keywords if k in description]

        elif any(k in description for k in storm_keywords):
            hazard_type = "storm"
            severity = "moderate"
            triggered_keywords = [k for k in storm_keywords if k in description]

        elif any(k in description for k in accident_keywords):
            hazard_type = "accident"
            severity = "high"
            triggered_keywords = [k for k in accident_keywords if k in description]

        else:
            # Default fallback: pick first 3 words
            hazard_type = "unknown"
            triggered_keywords = description.split()[:3]

        return {
            "hazard_type": hazard_type,
            "severity": severity,
            "triggered_keywords": triggered_keywords
        }
