# Feature: gharApi_v0_001 - Property Details API

## Constitution Reference

This feature specification is based on the GharGPT Backend Constitution (see `kitty-specs/memory/constitution.md` for full project context).

**Key Project Details:**

- Nx monorepo with Python FastAPI applications and shared libraries
- MongoDB for data persistence using Motor async driver
- Libraries in `libs/` for shared code (e.g., `mongodb-serve` for database operations)
- Applications in `apps/` (e.g., `api` for REST endpoints)

## Feature Overview

Develop a complete CRUD API service for property management, allowing clients to Create, Read, Update, and Delete property details from the MongoDB database. This API will support full property lifecycle management with filtering, pagination, and proper error handling.

## Technical Implementation

- **Framework**: Python FastAPI within Nx monorepo
- **Database Library**: `libs/mongodb-serve` with `properties` package for database transactions
- **API Location**: `apps/api` application
- **Endpoints**: Full CRUD operations (GET, POST, PUT, PATCH, DELETE) with proper REST conventions

## Properties Package in mongodb-serve Library

Created `libs/mongodb-serve/mongodb_serve/properties/` package containing:

### models.py

Pydantic models for Property data structures including:

- Property base model with all fields from schema
- PropertyCreate model for POST requests (without auto-generated fields)
- PropertyUpdate model for PATCH requests (all fields optional)
- Enums for property types, facing directions, etc.
- Nested models for location, budget, specifications, etc.

### service.py

Database service class with complete CRUD methods:

- **Read Operations**:
  - `get_all_properties()` - Fetch all properties with pagination
  - `get_property_by_id()` - Fetch single property by ID
  - `get_properties_by_filters()` - Filtered search with city, type, budget, verification status

- **Write Operations**:
  - `create_property()` - Create new property
  - `update_property()` - Update existing property
  - `delete_property()` - Delete property by ID

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

- **Router File**: `apps/api/api/properties.py` - Contains all property CRUD endpoints
- **Main App**: `apps/api/api/main.py` - Includes the properties router and initializes services

### 3. REST API Endpoints

#### GET /properties

- **Purpose**: Retrieve all properties with optional filtering and pagination
- **Query Parameters**: `skip`, `limit`, `city`, `property_type`, `min_budget`, `max_budget`, `is_verified`
- **Response**: List of Property objects

#### GET /properties/{property_id}

- **Purpose**: Retrieve a single property by ID
- **Path Parameter**: `property_id` (string)
- **Response**: Single Property object or 404 if not found

#### POST /properties

- **Purpose**: Create a new property
- **Request Body**: PropertyCreate model (without auto-generated fields like \_id, timestamps)
- **Response**: Created Property object with generated fields
- **Status Code**: 201 Created

#### PUT /properties/{property_id}

- **Purpose**: Update an entire property (full replacement)
- **Path Parameter**: `property_id` (string)
- **Request Body**: Complete PropertyUpdate model
- **Response**: Updated Property object or 404 if not found

#### PATCH /properties/{property_id}

- **Purpose**: Partially update a property
- **Path Parameter**: `property_id` (string)
- **Request Body**: Partial PropertyUpdate model (only changed fields)
- **Response**: Updated Property object or 404 if not found

#### DELETE /properties/{property_id}

- **Purpose**: Delete a property by ID
- **Path Parameter**: `property_id` (string)
- **Response**: 204 No Content or 404 if not found

### 4. Request/Response Models

- Use Pydantic models from `libs/mongodb-serve/mongodb_serve/properties.models`
- **Property**: Full property model for responses
- **PropertyCreate**: Model for POST requests (excludes auto-generated fields)
- **PropertyUpdate**: Model for PUT/PATCH requests (all fields optional)
- Ensure proper JSON serialization and validation

### 5. Error Handling

- Handle database connection errors
- Validate request data and query parameters
- Return appropriate HTTP status codes
- Provide meaningful error messages

### 6. Testing

- Unit tests for PropertyService methods
- Integration tests for all API endpoints
- Use existing pytest setup in `apps/api/tests/`
