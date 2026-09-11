import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=15
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"Could not fetch page. HTTP status: {response.status_code}"
        )

    if "Security Alert" in response.text:
        raise RuntimeError(
            "Website returned a security/anti-bot page instead of the property page."
        )

    return response.text

def scrape_property(url):
    html = fetch_page(url)

    soup = BeautifulSoup(html, "html.parser")

    return {
        "title": soup.title.get_text(strip=True) if soup.title else None,
        "images": [
            image.get("src")
            for image in soup.find_all("img")
            if image.get("src")
        ],
        "html": html
    }