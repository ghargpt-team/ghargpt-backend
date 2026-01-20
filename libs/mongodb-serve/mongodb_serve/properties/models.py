from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from bson import ObjectId


class PropertyType(str, Enum):
    PLOT = "Plot"
    HOUSE = "House"
    APARTMENT = "Apartment"
    SHOP = "Shop"
    COMMERCIAL_PLOT = "Commercial Plot"
    FARM_LAND = "Farm Land"


class Facing(str, Enum):
    NORTH = "North"
    SOUTH = "South"
    EAST = "East"
    WEST = "West"
    NORTH_EAST = "North-East"
    SOUTH_EAST = "South-East"
    NORTH_WEST = "North-West"
    SOUTH_WEST = "South-West"


class Furnished(str, Enum):
    FURNISHED = "Furnished"
    SEMI_FURNISHED = "Semi-Furnished"
    UNFURNISHED = "Unfurnished"


class PossessionStatus(str, Enum):
    UNDER_CONSTRUCTION = "Under Construction"
    READY_TO_MOVE = "Ready to Move"


class LandmarkType(str, Enum):
    PARK = "Park"
    SCHOOL = "School"
    HOSPITAL = "Hospital"
    MALL = "Mall"
    METRO = "Metro"
    AIRPORT = "Airport"


class Importance(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Severity(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class OwnerType(str, Enum):
    DEVELOPER = "Developer"
    OWNER = "Owner"
    BROKER = "Broker"


class Status(str, Enum):
    ACTIVE = "Active"
    SOLD = "Sold"
    RENTED = "Rented"
    INACTIVE = "Inactive"
    UNDER_REVIEW = "Under Review"


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class Location(BaseModel):
    city: str
    area: str
    address: str
    pincode: str
    state: str
    country: str
    coordinates: Coordinates


class Landmark(BaseModel):
    name: str
    distance: float  # in km
    type: LandmarkType


class Budget(BaseModel):
    amount: int  # in rupees
    currency: str = "INR"
    negotiable: bool
    price_per_sqft: Optional[int] = None


class MarketPrice(BaseModel):
    estimated_value: int
    last_updated: datetime
    appreciation_rate: float  # % per year


class Specifications(BaseModel):
    plot_size: Optional[int] = None  # sq yards
    built_up_area: Optional[int] = None  # sq ft
    carpet_area: Optional[int] = None  # sq ft
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    balconies: Optional[int] = None
    parking: Optional[int] = None
    floors: Optional[int] = None
    floor_number: Optional[int] = None
    facing: Optional[Facing] = None
    furnished: Optional[Furnished] = None
    possession_status: Optional[PossessionStatus] = None


class Benefit(BaseModel):
    category: str
    description: str
    importance: Importance


class Drawback(BaseModel):
    category: str
    description: str
    severity: Severity


class SimilarProperty(BaseModel):
    property_id: str  # ObjectId as string
    name: str
    similarity_score: float
    price_difference: int


class VerificationDocument(BaseModel):
    type: str
    document_url: str
    verified: bool


class Verification(BaseModel):
    verified_by: str
    verified_at: datetime
    verification_documents: List[VerificationDocument]


class Contact(BaseModel):
    phone: str
    email: str
    website: Optional[str] = None


class Owner(BaseModel):
    type: OwnerType
    name: str
    contact: Contact
    rera_id: Optional[str] = None


class RatingDistribution(BaseModel):
    star_5: int = Field(alias="5_star")
    star_4: int = Field(alias="4_star")
    star_3: int = Field(alias="3_star")
    star_2: int = Field(alias="2_star")
    star_1: int = Field(alias="1_star")


class Ratings(BaseModel):
    average: float
    count: int
    distribution: RatingDistribution


class Comment(BaseModel):
    user_id: str
    user_name: str
    rating: int
    comment: str
    posted_at: datetime
    helpful_count: int
    verified_buyer: bool


class Image(BaseModel):
    url: str
    type: str
    caption: str
    is_primary: bool


class Video(BaseModel):
    url: str
    type: str
    duration: int  # seconds


class Meta(BaseModel):
    title: str
    description: str
    keywords: List[str]


class AIMetadata(BaseModel):
    description_generated: bool
    price_prediction: int
    investment_score: float
    tags: List[str]


class Property(BaseModel):
    # MongoDB ObjectId as string
    id: Optional[str] = Field(default=None, alias="_id")

    # Basic Information
    name: str
    property_type: PropertyType
    age: int  # Years (0 for under construction)

    # Location Details
    location: Location

    # Nearby Landmarks
    landmarks: List[Landmark] = []

    # Financial Information
    budget: Budget
    market_price: Optional[MarketPrice] = None

    # Property Specifications
    specifications: Specifications

    # Benefits & Drawbacks
    benefits: List[Benefit] = []
    drawbacks: List[Drawback] = []

    # Similar Properties
    similar_properties: List[SimilarProperty] = []

    # Verification & Trust
    isVerified: bool
    verification: Optional[Verification] = None

    # Developer/Owner Information
    owner: Owner

    # Social Engagement
    ratings: Optional[Ratings] = None
    likes: int = 0
    views: int = 0
    inquiries: int = 0

    # Comments/Reviews
    comments: List[Comment] = []

    # Media
    images: List[Image] = []
    videos: List[Video] = []

    # SEO & Metadata
    slug: str
    meta: Meta

    # Status & Timestamps
    status: Status
    featured: bool
    created_at: datetime
    updated_at: datetime
    expires_at: Optional[datetime] = None

    # AI/ML Fields
    ai_metadata: Optional[AIMetadata] = None

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }


class PropertyCreate(BaseModel):
    """Model for creating new properties (excludes auto-generated fields)"""

    # Basic Information
    name: str
    property_type: PropertyType
    age: int  # Years (0 for under construction)

    # Location Details
    location: Location

    # Nearby Landmarks
    landmarks: List[Landmark] = []

    # Financial Information
    budget: Budget
    market_price: Optional[MarketPrice] = None

    # Property Specifications
    specifications: Specifications

    # Benefits & Drawbacks
    benefits: List[Benefit] = []
    drawbacks: List[Drawback] = []

    # Similar Properties
    similar_properties: List[SimilarProperty] = []

    # Verification & Trust
    isVerified: bool = False
    verification: Optional[Verification] = None

    # Developer/Owner Information
    owner: Owner

    # Social Engagement (start at 0)
    ratings: Optional[Ratings] = None
    likes: int = 0
    views: int = 0
    inquiries: int = 0

    # Comments/Reviews
    comments: List[Comment] = []

    # Media
    images: List[Image] = []
    videos: List[Video] = []

    # SEO & Metadata
    slug: str
    meta: Meta

    # Status & Timestamps (will be auto-generated)
    status: Status = Status.ACTIVE
    featured: bool = False
    expires_at: Optional[datetime] = None

    # AI/ML Fields
    ai_metadata: Optional[AIMetadata] = None


class PropertyUpdate(BaseModel):
    """Model for updating properties (all fields optional)"""

    # Basic Information
    name: Optional[str] = None
    property_type: Optional[PropertyType] = None
    age: Optional[int] = None

    # Location Details
    location: Optional[Location] = None

    # Nearby Landmarks
    landmarks: Optional[List[Landmark]] = None

    # Financial Information
    budget: Optional[Budget] = None
    market_price: Optional[MarketPrice] = None

    # Property Specifications
    specifications: Optional[Specifications] = None

    # Benefits & Drawbacks
    benefits: Optional[List[Benefit]] = None
    drawbacks: Optional[List[Drawback]] = None

    # Similar Properties
    similar_properties: Optional[List[SimilarProperty]] = None

    # Verification & Trust
    isVerified: Optional[bool] = None
    verification: Optional[Verification] = None

    # Developer/Owner Information
    owner: Optional[Owner] = None

    # Social Engagement
    ratings: Optional[Ratings] = None
    likes: Optional[int] = None
    views: Optional[int] = None
    inquiries: Optional[int] = None

    # Comments/Reviews
    comments: Optional[List[Comment]] = None

    # Media
    images: Optional[List[Image]] = None
    videos: Optional[List[Video]] = None

    # SEO & Metadata
    slug: Optional[str] = None
    meta: Optional[Meta] = None

    # Status & Timestamps
    status: Optional[Status] = None
    featured: Optional[bool] = None
    expires_at: Optional[datetime] = None

    # AI/ML Fields
    ai_metadata: Optional[AIMetadata] = None
