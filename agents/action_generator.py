class ActionGenerator:
    def generate(self, hazard_type, severity, description, nearby_resources):
        steps = []
        if hazard_type == "medical":
            steps.append({"action_text": "Ensure your mother uses her inhaler and stays away from humid air.", "safe": True, "note": ""})
        elif hazard_type == "flood":
            steps.append({"action_text": "Move to higher ground inside the home; bring essentials.", "safe": True, "note": ""})

        for r in nearby_resources:
            steps.append({
                "action_text": f"Nearest {r['type']} is {r['name']} ({r['distance']} km). Contact: {r['phone']}",
                "safe": True,
                "note": ""
            })

        return steps
