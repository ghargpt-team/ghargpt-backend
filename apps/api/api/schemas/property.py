"""
MongoDB Collection: properties

Index Strategy:
- location.city (ascending)
- property_type (ascending)
- budget.amount (ascending)
- isVerified (descending)
- created_at (descending)
- Compound: (location.city, property_type, budget.amount)
"""

from typing import List, Optional, Dict
from datetime import datetime
from enum import Enum

# MongoDB Document Structure
property_document = {
    "_id": "ObjectId",  # MongoDB auto-generated

    # Basic Information
    "name": "Premium Villa in Jubilee Hills",
    # Enum: Plot, House, Apartment, Shop, Commercial Plot, Farm Land
    "property_type": "House",
    "age": 2,  # Years (0 for under construction)

    # Location Details
    "location": {
        "city": "Hyderabad",
        "area": "Jubilee Hills",
        "address": "Road No 45, Jubilee Hills",
        "pincode": "500033",
        "state": "Telangana",
        "country": "India",
        "coordinates": {
            "latitude": 17.4326,
            "longitude": 78.4071
        }
    },

    # Nearby Landmarks
    "landmarks": [
        {
            "name": "KBR National Park",
            "distance": 2.5,  # in km
            "type": "Park"  # Park, School, Hospital, Mall, Metro, Airport
        },
        {
            "name": "Apollo Hospital",
            "distance": 3.0,
            "type": "Hospital"
        },
        {
            "name": "Jubilee Hills Metro Station",
            "distance": 1.2,
            "type": "Metro"
        }
    ],

    # Financial Information
    "budget": {
        "amount": 25000000,  # in rupees (2.5 Crore)
        "currency": "INR",
        "negotiable": True,
        "price_per_sqft": 8500
    },

    "market_price": {
        "estimated_value": 27000000,  # Current market estimate
        "last_updated": "2025-01-19T10:30:00Z",
        "appreciation_rate": 8.0  # % per year
    },

    # Property Specifications
    "specifications": {
        "plot_size": 300,  # sq yards
        "built_up_area": 3500,  # sq ft
        "carpet_area": 3000,  # sq ft
        "bedrooms": 4,
        "bathrooms": 5,
        "balconies": 2,
        "parking": 2,  # number of parking spots
        "floors": 3,  # total floors in building
        "floor_number": 2,  # which floor (for apartments)
        "facing": "East",  # North, South, East, West, North-East, etc.
        "furnished": "Semi-Furnished",  # Furnished, Semi-Furnished, Unfurnished
        "possession_status": "Ready to Move"  # Under Construction, Ready to Move
    },

    # Benefits & Drawbacks
    "benefits": [
        {
            "category": "Location",
            "description": "Prime location in Jubilee Hills with excellent connectivity",
            "importance": "High"  # High, Medium, Low
        },
        {
            "category": "Amenities",
            "description": "Gated community with 24/7 security, swimming pool, gym",
            "importance": "High"
        },
        {
            "category": "Investment",
            "description": "High appreciation area, 8-10% annual growth expected",
            "importance": "High"
        },
        {
            "category": "Legal",
            "description": "Clear title, RERA approved, bank loan approved",
            "importance": "High"
        }
    ],

    "drawbacks": [
        {
            "category": "Cost",
            "description": "Higher maintenance charges compared to nearby areas",
            "severity": "Medium"  # High, Medium, Low
        },
        {
            "category": "Traffic",
            "description": "Heavy traffic during peak hours on main road",
            "severity": "Medium"
        }
    ],

    # Similar Properties (References)
    "similar_properties": [
        {
            "property_id": "ObjectId('...')",  # Reference to another property
            "name": "Luxury Villa in Road No 36",
            "similarity_score": 0.85,  # 0-1 scale
            "price_difference": -2000000  # negative means cheaper
        }
    ],

    # Verification & Trust
    "isVerified": True,
    "verification": {
        "verified_by": "admin_user_id",
        "verified_at": "2025-01-15T10:00:00Z",
        "verification_documents": [
            {
                "type": "RERA Certificate",
                "document_url": "s3://documents/rera_cert.pdf",
                "verified": True
            },
            {
                "type": "Ownership Proof",
                "document_url": "s3://documents/ownership.pdf",
                "verified": True
            }
        ]
    },

    # Developer/Owner Information
    "owner": {
        "type": "Developer",  # Developer, Owner, Broker
        "name": "XYZ Constructions Pvt Ltd",
        "contact": {
            "phone": "+91-9876543210",
            "email": "sales@xyzconstructions.com",
            "website": "https://xyzconstructions.com"
        },
        "rera_id": "P02400012345"
    },

    # Social Engagement
    "ratings": {
        "average": 4.5,  # 0-5 scale
        "count": 127,
        "distribution": {
            "5_star": 85,
            "4_star": 30,
            "3_star": 8,
            "2_star": 3,
            "1_star": 1
        }
    },

    "likes": 342,
    "views": 5678,
    "inquiries": 89,  # Number of inquiry forms submitted

    # Comments/Reviews
    "comments": [
        {
            "user_id": "ObjectId('...')",
            "user_name": "Rajesh Kumar",
            "rating": 5,
            "comment": "Excellent property with great amenities. Highly recommended!",
            "posted_at": "2025-01-10T14:30:00Z",
            "helpful_count": 23,
            "verified_buyer": True
        }
    ],

    # Media
    "images": [
        {
            "url": "https://storage.ghargpt.com/properties/img1.jpg",
            "type": "Exterior",  # Exterior, Interior, Floor Plan, Location Map
            "caption": "Front view of the property",
            "is_primary": True
        }
    ],

    "videos": [
        {
            "url": "https://youtube.com/watch?v=...",
            "type": "Virtual Tour",
            "duration": 180  # seconds
        }
    ],

    # SEO & Metadata
    "slug": "premium-villa-jubilee-hills-hyderabad",
    "meta": {
        "title": "4 BHK Villa for Sale in Jubilee Hills, Hyderabad",
        "description": "Luxurious 4 BHK villa in prime Jubilee Hills location...",
        "keywords": ["villa", "jubilee hills", "hyderabad", "4 bhk", "luxury"]
    },

    # Status & Timestamps
    "status": "Active",  # Active, Sold, Rented, Inactive, Under Review
    "featured": True,  # Featured listing (paid promotion)
    "created_at": "2025-01-01T10:00:00Z",
    "updated_at": "2025-01-19T15:30:00Z",
    "expires_at": "2025-04-01T23:59:59Z",  # Listing expiry

    # AI/ML Fields
    "ai_metadata": {
        "description_generated": False,
        "price_prediction": 26500000,
        "investment_score": 8.5,  # 0-10 scale
        "tags": ["luxury", "gated-community", "prime-location", "investment"]
    }
}
