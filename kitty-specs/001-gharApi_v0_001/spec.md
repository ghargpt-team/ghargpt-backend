# Feature: gharApi_v0_001 - Property Details API

## Constitution Reference

This feature specification is based on the GharGPT Backend Constitution (see `kitty-specs/memory/constitution.md` for full project context).

**Key Project Details:**

- Nx monorepo with Python FastAPI applications and shared libraries
- MongoDB for data persistence using Motor async driver
- Libraries in `libs/` for shared code (e.g., `mongodb-serve` for database operations)
- Applications in `apps/` (e.g., `api` for REST endpoints)

## Feature Overview

Develop a GET API service to fetch property details from the MongoDB database. This API will allow clients to retrieve all properties or filter them based on various criteria.

## Technical Implementation

- **Framework**: Python FastAPI within Nx monorepo
- **Database Library**: `libs/mongodb-serve` with `properties` package for database transactions
- **API Location**: `apps/api` application
- **Endpoint**: `GET /properties` with optional query parameters for filtering

## Properties Package in mongodb-serve Library

Created `libs/mongodb-serve/mongodb_serve/properties/` package containing:

### models.py

Pydantic models for Property data structures including:

- Property base model with all fields from schema
- Enums for property types, facing directions, etc.
- Nested models for location, budget, specifications, etc.

### service.py

Database service class with methods:

- `get_all_properties()` - Fetch all properties with pagination
- `get_property_by_id()` - Fetch single property
- `get_properties_by_filters()` - Filtered search with city, type, budget, verification status
- CRUD operations for future use

## MongoDB Schema

Located at `apps/api/api/schemas/property.py`

### Collection: properties

### Index Strategy:

- `location.city` (ascending)
- `property_type` (ascending)
- `budget.amount` (ascending)
- `isVerified` (descending)
- `created_at` (descending)
- Compound: `(location.city, property_type, budget.amount)`

### Document Structure:

```json
{
  "_id": "ObjectId",
  "name": "Premium Villa in Jubilee Hills",
  "property_type": "House",
  "age": 2,
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
  "landmarks": [...],
  "budget": {
    "amount": 25000000,
    "currency": "INR",
    "negotiable": true,
    "price_per_sqft": 8500
  },
  "market_price": {...},
  "specifications": {...},
  "benefits": [...],
  "drawbacks": [...],
  "similar_properties": [...],
  "isVerified": true,
  "verification": {...},
  "owner": {...},
  "ratings": {...},
  "likes": 342,
  "views": 5678,
  "inquiries": 89,
  "comments": [...],
  "images": [...],
  "videos": [...],
  "slug": "premium-villa-jubilee-hills-hyderabad",
  "meta": {...},
  "status": "Active",
  "featured": true,
  "created_at": "2025-01-01T10:00:00Z",
  "updated_at": "2025-01-19T15:30:00Z",
  "expires_at": "2025-04-01T23:59:59Z",
  "ai_metadata": {...}
}
```

## API Development Plan

### 1. Database Connection

- Use existing MongoDB client from `mongodb_serve.client`
- Initialize PropertyService in the API application

### 2. API Endpoint Structure

- **Router File**: `apps/api/api/properties.py` - Contains the properties router with GET /properties endpoint
- **Main App**: `apps/api/api/main.py` - Includes the properties router and initializes services
- Query parameters: `skip`, `limit`, `city`, `property_type`, `min_budget`, `max_budget`, `is_verified`
- Response: List of Property objects

### 3. Response Model

- Use Pydantic models from `libs/mongodb-serve/mongodb_serve/properties.models`
- Ensure proper JSON serialization

### 4. Error Handling

- Handle database connection errors
- Validate query parameters
- Return appropriate HTTP status codes

### 5. Testing

- Unit tests for PropertyService methods
- Integration tests for API endpoint
- Use existing pytest setup in `apps/api/tests/`

## Dependencies

- Existing: `fastapi`, `motor`, `pydantic`, `pydantic-settings`
- Library: `mongodb-serve` (internal dependency)

## Next Steps

1. Implement the GET /properties endpoint in `apps/api/api/properties.py` (completed)
2. Include properties router in `apps/api/api/main.py` (completed)
3. Add query parameter validation
4. Test the endpoint with sample data
5. Add pagination metadata to response
6. Implement additional filtering options as needed
