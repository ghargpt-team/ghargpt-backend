# Implement PUT /properties/{property_id} endpoint

## Status

planned

## Description

Implement the PUT /properties/{property_id} endpoint for full property updates.

## Requirements

- Add PUT endpoint with path parameter `property_id`
- Accept PropertyUpdate model in request body
- Use PropertyService.update_property() method
- Return updated Property model or 404 if not found
- Perform full update (replace entire document)

## Implementation

1. Add the endpoint function to `apps/api/api/properties.py`
2. Use path parameter for property_id and PropertyUpdate model for request body
3. Convert PropertyUpdate to dict for database update
4. Call property_service.update_property(property_id, update_data)
5. Return the updated property or raise 404 if not found

## Files

- `apps/api/api/properties.py` - Add PUT endpoint
- `libs/mongodb-serve/mongodb_serve/properties/models.py` - May need PropertyUpdate model

## Testing

- Test with valid property ID and data (should update and return property)
- Test with non-existent ID (should return 404)
- Test with partial data (should update only provided fields)
- Verify all fields are properly updated

## Acceptance Criteria

- Endpoint performs full property updates
- Returns updated property data
- Returns 404 for non-existent properties
- Proper validation of request data
