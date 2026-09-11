from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup 
import json
from app.scraper.sources.magicbricks_property import parse_property_page

URL = "https://www.magicbricks.com/propertyDetails/2-BHK-1188-Sq-ft-Multistorey-Apartment-FOR-Sale-Devanahalli-in-Bangalore&id=4d423836343235393731"

options = Options()

driver = webdriver.Chrome(options=options)
property_data = parse_property_page(driver.page_source)

print("\nPROPERTY DATA")

for key, value in property_data.items():
    print(f"{key}: {value}")    
try:
    print("Opening page...")
    driver.get(URL)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    blocks = soup.find_all(
        "script",
        type="application/ld+json"
    )

    print("JSON-LD blocks:", len(blocks))

    for i, block in enumerate(blocks):
        data = json.loads(block.get_text(strip=True))

        print("\nBLOCK:", i)
        print("TYPE:", data.get("@type"))
    print("Title:", driver.title)
    print("URL:", driver.current_url)
    print("HTML length:", len(driver.page_source))

    with open(
        "data/input/magicbricks_property_selenium.html",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(driver.page_source)

    print("HTML saved.")

finally:
    driver.quit()