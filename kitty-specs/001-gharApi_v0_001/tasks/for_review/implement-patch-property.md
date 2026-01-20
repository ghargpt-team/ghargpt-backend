# Implement PATCH /properties/{property_id} endpoint

## Status

planned

## Description

Implement the PATCH /properties/{property_id} endpoint for partial property updates.

## Requirements

- Add PATCH endpoint with path parameter `property_id`
- Accept partial PropertyUpdate model in request body
- Use PropertyService.update_property() method
- Return updated Property model or 404 if not found
- Perform partial update (only update provided fields)

## Implementation

1. Add the endpoint function to `apps/api/api/properties.py`
2. Use path parameter for property_id and PropertyUpdate model for request body
3. Convert PropertyUpdate to dict, excluding unset fields
4. Call property_service.update_property(property_id, update_data)
5. Return the updated property or raise 404 if not found

## Files

- `apps/api/api/properties.py` - Add PATCH endpoint
- `libs/mongodb-serve/mongodb_serve/properties/models.py` - May need PropertyUpdate model

## Testing

- Test with valid property ID and partial data (should update only provided fields)
- Test with non-existent ID (should return 404)
- Test with empty update data (should return current property unchanged)
- Verify only specified fields are updated

## Acceptance Criteria

- Endpoint performs partial property updates
- Returns updated property data
- Returns 404 for non-existent properties
- Only provided fields are updated
