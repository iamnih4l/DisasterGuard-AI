class MemoryBank:
    def __init__(self):
        self.memory = {}

    def store(self, user_id, key, value):
        if user_id not in self.memory:
            self.memory[user_id] = {}
        self.memory[user_id][key] = value

    def retrieve(self, user_id, key):
        return self.memory.get(user_id, {}).get(key)
