from app.ai.dev_provider import DevAIProvider


class AIService:

    def __init__(self):
        self.provider = DevAIProvider()

    def generate(self, prompt):
        return self.provider.generate(prompt)