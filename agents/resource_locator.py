class ResourceLocator:
    def get_nearby(self, lat, lon):
        # Dummy resources for testing
        return [
            {"type": "hospital", "name": "Green Cross Hospital", "lat": 12.918, "lon": 74.855, "phone": "+91-9876500000", "distance": 0.35},
            {"type": "shelter", "name": "City Central Shelter", "lat": 12.91, "lon": 74.858, "phone": "+91-9876543210", "distance": 0.6},
            {"type": "fire_station", "name": "Metro Fire & Rescue", "lat": 12.92, "lon": 74.86, "phone": "101", "distance": 0.71}
        ]
