class SessionHistory:
    def __init__(self):
        self.results = []


    def add(self, text: str):
        self.results.append(text)


    def clear(self):
        self.results.clear()