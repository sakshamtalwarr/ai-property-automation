import json
from bs4 import BeautifulSoup


def parse_property_page(html):
    soup = BeautifulSoup(html, "html.parser")

    blocks = soup.find_all(
        "script",
        type="application/ld+json"
    )

    for block in blocks:
        try:
            data = json.loads(block.get_text(strip=True))
        except json.JSONDecodeError:
            continue

        data_type = data.get("@type", [])

        if isinstance(data_type, str):
            data_type = [data_type]

        if "RealEstateListing" not in data_type:
            continue

        main_entity = data.get("mainEntity", {})
        address = main_entity.get("address", {})
        offers = data.get("offers", {})
        geo = main_entity.get("geo", {})

        return {
            "title": data.get("name"),
            "description": data.get("description"),
            "url": data.get("url"),
            "price": offers.get("price"),
            "currency": offers.get("priceCurrency"),
            "bedrooms": main_entity.get("numberOfBedrooms"),
            "bathrooms": main_entity.get("numberOfBathroomsTotal"),
            "location": address.get("addressLocality"),
            "region": address.get("addressRegion"),
            "latitude": geo.get("latitude"),
            "longitude": geo.get("longitude"),
            "image": data.get("image", {}).get("url"),
        }

    raise RuntimeError(
        "No RealEstateListing JSON-LD found."
    )