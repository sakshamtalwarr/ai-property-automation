from bs4 import BeautifulSoup

from app.config import DEFAULT_SOURCE
from app.scraper.sources.registry import get_source


def scrape_property(url, source_name=DEFAULT_SOURCE):
    source = get_source(source_name)

    html = source.fetch(url)

    soup = BeautifulSoup(html, "html.parser")

    images = []

    for image in soup.select("img"):
        src = image.get("src")

        if src:
            images.append(src)

    return {
        "title": soup.title.get_text(strip=True) if soup.title else None,
        "location": soup.select_one(".location").get_text(strip=True),
        "price": soup.select_one(".price").get_text(strip=True),
        "bedrooms": soup.select_one(".bedrooms").get_text(strip=True),
        "bathrooms": soup.select_one(".bathrooms").get_text(strip=True),
        "area_sqft": soup.select_one(".area").get_text(strip=True),
        "description": soup.select_one(".description").get_text(strip=True),
        "images": images,
    }