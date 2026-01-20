# Implement GET /properties/{property_id} endpoint

## Status

planned

## Description

Implement the GET /properties/{property_id} endpoint to retrieve a single property by its ID.

## Requirements

- Add GET endpoint with path parameter `property_id`
- Use PropertyService.get_property_by_id() method
- Return Property model or 404 if not found
- Include proper error handling for database errors
- Add endpoint to properties router

## Implementation

1. Add the endpoint function to `apps/api/api/properties.py`
2. Use path parameter validation for property_id
3. Call property_service.get_property_by_id(property_id)
4. Return the property data or raise HTTPException with 404 status
5. Handle any database exceptions

## Files

- `apps/api/api/properties.py` - Add GET endpoint

## Testing

- Test with valid property ID (should return property data)
- Test with invalid/non-existent ID (should return 404)
- Test with malformed ID (should return 400)
- Verify response matches Property model schema

## Acceptance Criteria

- Endpoint returns single property by ID
- Returns 404 for non-existent properties
- Proper error handling for database issues
- Response validates against Property model
