from app.scraper.property_scraper import scrape_property
from app.parser.property_parser import parse_property_data
from app.parser.property import Property
from app.ai.service import AIService


def main():
    raw_data = scrape_property(
        "data/input/property_page.html"
    )

    clean_data = parse_property_data(raw_data)

    property = Property(**clean_data)

    ai = AIService()

    prompt = f"""
Create marketing content for this property:

Title: {property.title}
Location: {property.location}
Price: ₹{property.price}
Bedrooms: {property.bedrooms}
Bathrooms: {property.bathrooms}
Area: {property.area_sqft} sq ft
Description: {property.description}
"""

    result = ai.generate(prompt)

    print(result)


if __name__ == "__main__":
    main()