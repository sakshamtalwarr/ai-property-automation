from app.parser.loader import load_properties
from app.parser.property import Property
from app.parser.serializer import save_property


def main():
    properties = load_properties("data/input/properties.json")

    for property_data in properties:
        property = Property(
            title=property_data["title"],
            location=property_data["location"],
            price=property_data["price"],
            bedrooms=property_data["bedrooms"],
            bathrooms=property_data["bathrooms"],
            area_sqft=property_data["area_sqft"],
            description=property_data["description"]
        )

        print(f"Processing: {property.title}")

        output_file = (
            f"data/output/"
            f"{property.title.lower().replace(' ', '_')}.json"
        )

        save_property(property, output_file)

    print("All properties processed.")


if __name__ == "__main__":
    main()