from app.ai.providers import get_provider


class AIService:

    def __init__(self, provider="dev"):
        self.provider = get_provider(provider)

    def generate(self, prompt):
        return self.provider.generate(prompt)