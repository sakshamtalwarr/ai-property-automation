class PropertyWorkflow:

    def __init__(self, property):
        self.property = property

    def check_images(self):
        if self.property.images:
            return {
                "status": "images_available",
                "action": "use_existing_images"
            }

        return {
            "status": "images_missing",
            "action": "generate_images"
        }