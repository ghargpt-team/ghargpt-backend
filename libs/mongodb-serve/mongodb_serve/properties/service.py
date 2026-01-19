from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from .models import Property


class PropertyService:
    def __init__(self, database: AsyncIOMotorDatabase):
        self.database = database
        self.collection = database.properties

    async def get_all_properties(self, skip: int = 0, limit: int = 100) -> List[Property]:
        """Fetch all properties with pagination."""
        cursor = self.collection.find().skip(skip).limit(limit)
        documents = await cursor.to_list(length=None)
        return [Property(**doc) for doc in documents]

    async def get_property_by_id(self, property_id: str) -> Optional[Property]:
        """Fetch a single property by ID."""
        doc = await self.collection.find_one({"_id": property_id})
        return Property(**doc) if doc else None

    async def get_properties_by_filters(
        self,
        city: Optional[str] = None,
        property_type: Optional[str] = None,
        min_budget: Optional[int] = None,
        max_budget: Optional[int] = None,
        is_verified: Optional[bool] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[Property]:
        """Fetch properties with filters."""
        query = {}
        if city:
            query["location.city"] = city
        if property_type:
            query["property_type"] = property_type
        if min_budget or max_budget:
            budget_query = {}
            if min_budget:
                budget_query["$gte"] = min_budget
            if max_budget:
                budget_query["$lte"] = max_budget
            query["budget.amount"] = budget_query
        if is_verified is not None:
            query["isVerified"] = is_verified

        cursor = self.collection.find(query).skip(skip).limit(limit)
        documents = await cursor.to_list(length=None)
        return [Property(**doc) for doc in documents]

    async def create_property(self, property_data: Property) -> Property:
        """Create a new property."""
        doc = property_data.dict(by_alias=True, exclude_unset=True)
        result = await self.collection.insert_one(doc)
        doc["_id"] = result.inserted_id
        return Property(**doc)

    async def update_property(self, property_id: str, update_data: dict) -> Optional[Property]:
        """Update a property."""
        result = await self.collection.update_one(
            {"_id": property_id},
            {"$set": update_data}
        )
        if result.modified_count:
            return await self.get_property_by_id(property_id)
        return None

    async def delete_property(self, property_id: str) -> bool:
        """Delete a property."""
        result = await self.collection.delete_one({"_id": property_id})
        return result.deleted_count > 0
