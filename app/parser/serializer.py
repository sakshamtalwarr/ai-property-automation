import json


def property_to_dict(property):
    return {
        "title": property.title,
        "location": property.location,
        "price": property.price,
        "bedrooms": property.bedrooms,
        "bathrooms": property.bathrooms,
        "area_sqft": property.area_sqft,
        "description": property.description,
    }


def save_property(property, file_path):
    data = property_to_dict(property)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)