from bs4 import BeautifulSoup


def scrape_property(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    property_data = {
        "title": soup.select_one(".property-title").get_text(strip=True),
        "location": soup.select_one(".location").get_text(strip=True),
        "price": soup.select_one(".price").get_text(strip=True),
        "bedrooms": soup.select_one(".bedrooms").get_text(strip=True),
        "bathrooms": soup.select_one(".bathrooms").get_text(strip=True),
        "area_sqft": soup.select_one(".area").get_text(strip=True),
        "description": soup.select_one(".description").get_text(strip=True),
    }

    return property_data