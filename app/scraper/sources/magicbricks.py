import json

from bs4 import BeautifulSoup

from app.scraper.sources.base import PropertySource


class MagicBricksSource(PropertySource):

    def fetch(self, url):
        raise NotImplementedError(
            "Individual property fetching is not implemented yet."
        )

    def parse_listings(self, html):
        soup = BeautifulSoup(html, "html.parser")

        blocks = soup.find_all(
            "script",
            type="application/ld+json"
        )

        if not blocks:
            raise RuntimeError(
                "No JSON-LD data found on MagicBricks page."
            )

        data = json.loads(
            blocks[0].get_text(strip=True)
        )

        listings = []

        for item in data.get("itemListElement", []):
            property_data = item.get("item", {})

            address = property_data.get(
                "address",
                {}
            )

            listings.append({
                "title": property_data.get("name"),
                "url": property_data.get("url"),
                "bedrooms": property_data.get(
                    "numberOfBedrooms"
                ),
                "bathrooms": property_data.get(
                    "numberOfBathroomsTotal"
                ),
                "image": property_data.get("image"),
                "location": address.get(
                    "addressLocality"
                ),
                "region": address.get(
                    "addressRegion"
                ),
            })

        return listings

    def scrape_listings(self, url):
        html = self._fetch_with_requests(url)

        return self.parse_listings(html)

    def _fetch_with_requests(self, url):
        import requests

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Could not fetch MagicBricks page. "
                f"HTTP status: {response.status_code}"
            )

        return response.text