# Task: Separate API Endpoint into Router

## Status: for_review

## Description

Refactor API endpoint from main.py into separate router file for better organization.

## Requirements

- Create `apps/api/api/properties.py` with APIRouter
- Move GET /properties endpoint to router
- Update main.py to include router
- Maintain all functionality and error handling

## Implementation

- Created properties router in separate file
- Implemented service initialization function
- Updated main.py to import and include router
- Preserved all query parameters and validation

## Files Created/Modified

- `apps/api/api/properties.py` (new)
- `apps/api/api/main.py` (modified)

## Testing

- Verify endpoint still accessible
- Test all query parameters work
- Check error handling unchanged
- Ensure router integration works

## Acceptance Criteria

- Clean separation of concerns
- All functionality preserved
- No breaking changes to API
- Better code organization
