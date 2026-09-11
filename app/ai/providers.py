from app.ai.dev_provider import DevAIProvider


PROVIDERS = {
    "dev": DevAIProvider,
}


def get_provider(name):
    provider_class = PROVIDERS.get(name)

    if provider_class is None:
        raise ValueError(f"Unknown AI provider: {name}")

    return provider_class()