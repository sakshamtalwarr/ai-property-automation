import re


def parse_price(price):
    price = price.replace("₹", "").strip()

    if "Crore" in price:
        value = float(price.replace("Crore", "").strip())
        return int(value * 10_000_000)

    if "Lakh" in price:
        value = float(price.replace("Lakh", "").strip())
        return int(value * 100_000)

    return int(re.sub(r"[^\d]", "", price))


def parse_number(value):
    match = re.search(r"\d+", value)

    if match:
        return int(match.group())

    return None


def parse_property_data(data):
    return {
        "title": data["title"],
        "location": data["location"],
        "price": parse_price(data["price"]),
        "bedrooms": parse_number(data["bedrooms"]),
        "bathrooms": parse_number(data["bathrooms"]),
        "area_sqft": parse_number(data["area_sqft"]),
        "description": data["description"],
    }