class InMemorySessionService:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        session_id = f"session_{len(self.sessions)+1}"
        self.sessions[user_id] = session_id
        return session_id

    def get_session(self, user_id):
        return self.sessions.get(user_id)
