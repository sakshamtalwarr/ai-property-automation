class PropertyWorkflow:

    def __init__(self, property):
        self.property = property

    def check_images(self):
        if hasattr(self.property, "images") and self.property.images:
            return "images_available"

        return "images_missing"