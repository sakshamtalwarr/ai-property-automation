import json

from app.ai.provider import AIProvider


class DevAIProvider(AIProvider):

    def generate(self, prompt):
        return json.dumps({
            "headline": "Luxury Living in Whitefield",
            "description": (
                "Experience spacious and modern living in this "
                "luxury 3BHK apartment in Whitefield, Bangalore."
            ),
            "selling_points": [
                "Spacious 3BHK layout",
                "Prime Whitefield location",
                "1800 sq ft of living space",
                "Modern amenities",
                "Excellent connectivity"
            ],
            "social_caption": (
                "Discover luxury living in Whitefield. "
                "A spacious 3BHK designed for modern living."
            )
        }, indent=4)