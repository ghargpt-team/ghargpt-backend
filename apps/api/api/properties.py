from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from mongodb_serve.properties.service import PropertyService
from mongodb_serve.properties.models import Property, PropertyCreate, PropertyUpdate

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


@router.get("/properties/{property_id}", response_model=Property)
async def get_property_by_id(property_id: str):
    """
    Get a single property by its ID.
    """
    if not property_service:
        raise HTTPException(
            status_code=500, detail="Property service not initialized")

    try:
        property_data = await property_service.get_property_by_id(property_id)
        if not property_data:
            raise HTTPException(status_code=404, detail="Property not found")
        return property_data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")


@router.post("/properties", response_model=Property, status_code=201)
async def create_property(property_data: PropertyCreate):
    """
    Create a new property.
    """
    if not property_service:
        raise HTTPException(
            status_code=500, detail="Property service not initialized")

    try:
        created_property = await property_service.create_property(property_data)
        return created_property
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")


@router.put("/properties/{property_id}", response_model=Property)
async def update_property(property_id: str, property_data: PropertyUpdate):
    """
    Update an entire property (full replacement).
    """
    if not property_service:
        raise HTTPException(
            status_code=500, detail="Property service not initialized")

    try:
        # Convert PropertyUpdate to dict for database update
        update_dict = property_data.dict(exclude_unset=True)
        if not update_dict:
            # If no fields provided, return current property
            current_property = await property_service.get_property_by_id(property_id)
            if not current_property:
                raise HTTPException(
                    status_code=404, detail="Property not found")
            return current_property

        updated_property = await property_service.update_property(property_id, update_dict)
        if not updated_property:
            raise HTTPException(status_code=404, detail="Property not found")
        return updated_property
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")


@router.patch("/properties/{property_id}", response_model=Property)
async def partial_update_property(property_id: str, property_data: PropertyUpdate):
    """
    Partially update a property (only provided fields).
    """
    if not property_service:
        raise HTTPException(
            status_code=500, detail="Property service not initialized")

    try:
        # Convert PropertyUpdate to dict, excluding unset fields for partial update
        update_dict = property_data.dict(exclude_unset=True)
        if not update_dict:
            # If no fields provided, return current property
            current_property = await property_service.get_property_by_id(property_id)
            if not current_property:
                raise HTTPException(
                    status_code=404, detail="Property not found")
            return current_property

        updated_property = await property_service.update_property(property_id, update_dict)
        if not updated_property:
            raise HTTPException(status_code=404, detail="Property not found")
        return updated_property
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")


@router.delete("/properties/{property_id}", status_code=204)
async def delete_property(property_id: str):
    """
    Delete a property by its ID.
    """
    if not property_service:
        raise HTTPException(
            status_code=500, detail="Property service not initialized")

    try:
        deleted = await property_service.delete_property(property_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Property not found")
        return  # 204 No Content - no response body
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")
