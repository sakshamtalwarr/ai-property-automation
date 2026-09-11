import json

from app.ai.service import AIService


def generate_property_content(property):
    ai = AIService()

    prompt = f"""
Create professional real estate marketing content for this property.

Property:
Title: {property.title}
Location: {property.location}
Price: ₹{property.price}
Bedrooms: {property.bedrooms}
Bathrooms: {property.bathrooms}
Area: {property.area_sqft} sq ft
Description: {property.description}

Generate:
1. A short marketing headline
2. A professional property description
3. Five selling points
4. A short social media caption
"""

    result = ai.generate(prompt)

    return json.loads(result)