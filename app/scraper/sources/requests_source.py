import requests

from app.scraper.sources.base import PropertySource


class RequestsPropertySource(PropertySource):

    def fetch(self, url):
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
                "Website returned a security/anti-bot page."
            )

        return response.text