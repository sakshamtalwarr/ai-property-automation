from app.scraper.property_scraper import scrape_property


def main():
    property_data = scrape_property("data/input/property_page.html")

    print(property_data)


if __name__ == "__main__":
    main()