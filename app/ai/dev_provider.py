from app.ai.provider import AIProvider


class DevAIProvider(AIProvider):

    def generate(self, prompt):
        return f"Generated content for: {prompt}"