class Property:
    def __init__(
        self,
        title,
        location,
        price,
        bedrooms,
        bathrooms,
        area_sqft,
        description,
        images=None
    ):
        self.title = title
        self.location = location
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.area_sqft = area_sqft
        self.description = description
        self.images = images or []