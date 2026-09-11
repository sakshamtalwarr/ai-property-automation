import json

from app.scraper.property_scraper import scrape_property
from app.parser.property_parser import parse_property_data
from app.parser.property import Property
from app.ai.content_generator import generate_property_content


def main():
    raw_data = scrape_property(
        "data/input/property_page.html"
    )

    clean_data = parse_property_data(raw_data)

    property = Property(**clean_data)

    print(f"Processing: {property.title}")

    content = generate_property_content(property)

    output = {
        "property": clean_data,
        "content": content
    }

    with open(
        "data/output/ai/generated_content.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(output, file, indent=4, ensure_ascii=False)

    print("AI content generated successfully.")


if __name__ == "__main__":
    main()