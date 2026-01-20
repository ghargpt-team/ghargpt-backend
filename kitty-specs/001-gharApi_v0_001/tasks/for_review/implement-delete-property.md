# Implement DELETE /properties/{property_id} endpoint

## Status

planned

## Description

Implement the DELETE /properties/{property_id} endpoint to remove properties from the database.

## Requirements

- Add DELETE endpoint with path parameter `property_id`
- Use PropertyService.delete_property() method
- Return 204 No Content on success or 404 if not found
- Include proper error handling for database errors

## Implementation

1. Add the endpoint function to `apps/api/api/properties.py`
2. Use path parameter validation for property_id
3. Call property_service.delete_property(property_id)
4. Return 204 status if deleted, 404 if not found
5. Handle any database exceptions

## Files

- `apps/api/api/properties.py` - Add DELETE endpoint

## Testing

- Test with valid property ID (should return 204 and remove property)
- Test with non-existent ID (should return 404)
- Test with malformed ID (should return 400)
- Verify property is actually removed from database

## Acceptance Criteria

- Endpoint successfully deletes properties
- Returns 204 for successful deletion
- Returns 404 for non-existent properties
- Property is permanently removed from database
