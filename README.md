# DisasterGuard AI

![DisasterGuard AI](https://img.shields.io/badge/DisasterGuard-AI-blue?style=for-the-badge)  
**AI-powered multi-agent emergency response system.**

---

## 🚀 Overview

**DisasterGuard AI** is an intelligent multi-agent system designed to assist in emergencies like floods, fires, medical crises, and more. It detects hazards, finds nearby resources, prioritizes threats, and provides actionable emergency steps in real time.  

**Built for:** Mini projects, AI Agent competitions, and real-world emergency simulations.

---

## 🌟 Features

- **Hazard Classification:** Floods, fires, medical emergencies, storms, etc.
- **Priority Scoring:** Calculates urgency for action (Normal → Critical)
- **Nearby Resource Detection:** Hospitals, shelters, fire stations
- **Action Recommendations:** Step-by-step instructions to stay safe
- **Sessions & Memory Management:** Tracks context and previous emergencies
- **Modular Multi-Agent System:** Classifier, Prioritizer, Resource Locator, Action Generator
- **Normalized JSON Output:** Easy to integrate with apps or dashboards

---

## 🛠 Tech Stack

- **Python 3.11+**
- **LLM-powered Agents** for hazard classification and emergency planning
- **Multi-agent Architecture**: DisasterOrchestrator orchestrating agents
- **Memory & Sessions**: InMemorySessionService and MemoryBank
- **Optional APIs**: Google Maps / OpenStreetMap for resources

---

## 📝 Quick Start

```python
from disasterguard import DisasterOrchestrator, InMemorySessionService, MemoryBank

# Initialize services
sessions = InMemorySessionService()
memory = MemoryBank()

# Initialize orchestrator
orch = DisasterOrchestrator(sessions, memory)

# Sample input
user_id = "user_nihal"
location_text = "Kadri, Mangalore"
description = "Water is rising fast and my mother has asthma"

# Get AI-generated emergency plan
response = orch.handle_request(user_id, location_text, description)

# Print structured response
import json
print(json.dumps(response, indent=2))

{
  "location": {"lat": 12.915, "lon": 74.856, "place_id": "mangalore_lower_1"},
  "risk": {"hazard_type": "medical", "severity": "high", "immediate_threats": ["asthma", "water", "rising"], "recommended_immediacy": "now"},
  "priority": {"priority_score": 100, "priority_level": "CRITICAL"},
  "nearby_resources": [
    {"type": "hospital", "name": "Green Cross Hospital", "lat": 12.918, "lon": 74.855, "phone": "+91-9876500000", "distance": 0.35},
    {"type": "shelter", "name": "City Central Shelter", "lat": 12.91, "lon": 74.858, "phone": "+91-9876543210", "distance": 0.6}
  ],
  "recommended_actions": [
    {"text": "Ensure your mother uses her inhaler and stays away from humid air.", "safe": true, "note": ""},
    {"text": "Nearest hospital is Green Cross Hospital (0.35 km). Contact: +91-9876500000", "safe": true, "note": ""}
  ],
  "session_id": "session_123"
}
```


##🎯 Project Card

Feature	Status

Multi-agent System	- ✅ Complete
Hazard Classification -	✅ Complete
Priority Scoring - ✅ Complete
Nearby Resource Detection -	✅ Complete
Action Generation -	✅ Complete
Sessions & Memory -	✅ Complete
Normalized Output -	✅ Complete

##Agent Architecture Diagram:

[User Input] --> [DisasterOrchestrator] --> [Classifier Agent]
                                      --> [Prioritizer Agent]
                                      --> [Resource Locator Agent]
                                      --> [Action Generator Agent]
                                      --> [Normalized Output]

##📈 Future Enhancements

-Real-time geolocation tracking for mobile users

-Integration with government disaster alerts

-Voice-based emergency reporting

-Multi-language support

-Cloud deployment & scalability

-A2A communication for multiple agents

🤝 Contributing

-Open issues or PRs with bug fixes or new hazard types

-Suggest new features for better emergency response

-Share datasets for improved resource recommendations
