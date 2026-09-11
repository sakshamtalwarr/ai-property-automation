import json

from bs4 import BeautifulSoup


html = open(
    "data/input/magicbricks.html",
    encoding="utf-8"
).read()

soup = BeautifulSoup(html, "html.parser")

blocks = soup.find_all(
    "script",
    type="application/ld+json"
)

data = json.loads(
    blocks[0].get_text(strip=True)
)

properties = data["itemListElement"]

for item in properties:
    property_data = item["item"]

    print("Title:", property_data.get("name"))
    print("Bedrooms:", property_data.get("numberOfBedrooms"))
    print("Bathrooms:", property_data.get("numberOfBathroomsTotal"))
    print("URL:", property_data.get("url"))
    print("Image:", property_data.get("image"))

    address = property_data.get("address", {})

    print("Location:", address.get("addressLocality"))
    print("Region:", address.get("addressRegion"))

    print("-" * 60)