from core.session_service import InMemorySessionService
from core.memory_bank import MemoryBank
from agents.hazard_classifier import HazardClassifier
from agents.emergency_prioritizer import EmergencyPrioritizer
from agents.resource_locator import ResourceLocator
from agents.action_generator import ActionGenerator

def normalize_disaster_response(raw):
    return {
        "location": raw["geo"],
        "risk": raw["risk"],
        "priority": raw["priority"],
        "nearby_resources": raw.get("resources", []),
        "recommended_actions": [
            {"text": step["action_text"], "safe": step.get("safe", True), "note": step.get("note","")}
            for step in raw.get("verified_plan", [])
        ],
        "session_id": raw["session_id"]
    }

class DisasterOrchestrator:
    def __init__(self, session_service, memory_bank):
        self.sessions = session_service
        self.memory = memory_bank
        self.classifier = HazardClassifier()
        self.prioritizer = EmergencyPrioritizer()
        self.resources = ResourceLocator()
        self.actions = ActionGenerator()

    def handle_request(self, user_id, location_text, description):
        session_id = self.sessions.create_session(user_id)
        geo = {"lat": 12.915, "lon": 74.856, "place_id": location_text.replace(" ", "_").lower()}

        classification = self.classifier.classify(description)
        risk = {
            "hazard_type": classification["hazard_type"],
            "severity": classification["severity"],
            "immediate_threats": classification["triggered_keywords"],
            "recommended_immediacy": "now" if classification["severity"] in ["high","extreme"] else "soon"
        }

        resources = self.resources.get_nearby(geo["lat"], geo["lon"])
        verified_steps = self.actions.generate(classification["hazard_type"], classification["severity"], description, resources)
        priority = self.prioritizer.score(classification["hazard_type"], classification["severity"], description, classification["triggered_keywords"], resources)

        raw_output = {
            "geo": geo,
            "risk": risk,
            "resources": resources,
            "verified_plan": verified_steps,
            "priority": priority,
            "session_id": session_id
        }

        return normalize_disaster_response(raw_output)
