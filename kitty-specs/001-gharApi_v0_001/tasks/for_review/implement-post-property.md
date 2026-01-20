# Implement POST /properties endpoint

## Status

planned

## Description

Implement the POST /properties endpoint to create new properties in the database.

## Requirements

- Add POST endpoint that accepts PropertyCreate model in request body
- Use PropertyService.create_property() method
- Return created Property model with generated ID and timestamps
- Return 201 Created status code
- Include proper validation and error handling

## Implementation

1. Add the endpoint function to `apps/api/api/properties.py`
2. Use PropertyCreate model for request body validation
3. Call property_service.create_property(property_data)
4. Return the created property with 201 status code
5. Handle validation errors and database exceptions

## Files

- `apps/api/api/properties.py` - Add POST endpoint
- `libs/mongodb-serve/mongodb_serve/properties/models.py` - May need PropertyCreate model

## Testing

- Test with valid property data (should create and return property)
- Test with invalid data (should return 422 validation error)
- Test with missing required fields (should return 422)
- Verify generated ID and timestamps are included in response

## Acceptance Criteria

- Endpoint creates new properties successfully
- Returns 201 status code with created property data
- Proper validation of request data
- Generated fields (ID, timestamps) are included in response
