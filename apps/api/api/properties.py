from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from mongodb_serve.properties.service import PropertyService
from mongodb_serve.properties.models import Property

# Create router for properties endpoints
router = APIRouter()

# Note: PropertyService should be initialized with database in main.py
property_service: Optional[PropertyService] = None


def init_property_service(database):
    """Initialize the property service with database connection."""
    global property_service
    property_service = PropertyService(database)


@router.get("/properties", response_model=List[Property])
async def get_properties(
    skip: int = Query(0, ge=0, description="Number of properties to skip"),
    limit: int = Query(100, ge=1, le=1000,
                       description="Maximum number of properties to return"),
    city: Optional[str] = Query(None, description="Filter by city"),
    property_type: Optional[str] = Query(
        None, description="Filter by property type"),
    min_budget: Optional[int] = Query(
        None, ge=0, description="Minimum budget amount"),
    max_budget: Optional[int] = Query(
        None, ge=0, description="Maximum budget amount"),
    is_verified: Optional[bool] = Query(
        None, description="Filter by verification status")
):
    """
    Get all properties with optional filtering and pagination.
    """
    if not property_service:
        raise HTTPException(
            status_code=500, detail="Property service not initialized")

    try:
        if min_budget and max_budget and min_budget > max_budget:
            raise HTTPException(
                status_code=400, detail="min_budget cannot be greater than max_budget")

        properties = await property_service.get_properties_by_filters(
            city=city,
            property_type=property_type,
            min_budget=min_budget,
            max_budget=max_budget,
            is_verified=is_verified,
            skip=skip,
            limit=limit
        )
        return properties
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")
