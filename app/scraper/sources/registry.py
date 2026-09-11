from app.scraper.sources.requests_source import RequestsPropertySource
from app.scraper.sources.magicbricks import MagicBricksSource


SOURCES = {
    "requests": RequestsPropertySource,
    "magicbricks": MagicBricksSource,
}


def get_source(name):
    source_class = SOURCES.get(name)

    if source_class is None:
        raise ValueError(f"Unknown source: {name}")

    return source_class()


def get_available_sources():
    return list(SOURCES.keys())