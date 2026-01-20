# Railway Deployment

This project is configured for deployment on Railway using Docker.

## Files Created

- `Dockerfile` - Multi-stage Docker build for the FastAPI application
- `.dockerignore` - Excludes unnecessary files from Docker build context

## Deployment Steps

1. Go to [Railway](https://railway.com/new)
2. Connect your GitHub repository
3. Railway will automatically detect the Dockerfile and deploy
4. Set environment variables in Railway dashboard:
   - `MONGODB_URL` - Your MongoDB connection string
   - Any other environment variables from your `.env` file

## Environment Variables

Make sure to set these in your Railway project settings:

```bash
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/database
# Add any other variables from your .env file
```

**Note:** Railway automatically sets the `PORT` environment variable. The application is configured to use this port.

## Troubleshooting

If you encounter "Poetry could not find a pyproject.toml file" error:

- The Dockerfile has been updated to properly handle the monorepo structure
- The application runs from the correct directory with Poetry configuration
- Re-deploy after pushing the latest changes

## Health Check

The application includes a health check that verifies the `/docs` endpoint is accessible.

## Port Configuration

The application runs on port 8000 by default, but Railway will automatically assign and route traffic to the correct port.
