from app.scraper.property_scraper import scrape_property
from app.parser.property_parser import parse_property_data
from app.parser.property import Property
from app.parser.serializer import save_property


def main():
    raw_data = scrape_property(
        "data/input/property_page.html"
    )

    clean_data = parse_property_data(raw_data)

    property = Property(**clean_data)

    print(f"Property: {property.title}")
    print(f"Price: ₹{property.price}")
    print(f"Bedrooms: {property.bedrooms}")
    print(f"Area: {property.area_sqft} sq ft")

    save_property(
        property,
        "data/output/scraped_property.json"
    )

    print("Property saved successfully.")


if __name__ == "__main__":
    main()