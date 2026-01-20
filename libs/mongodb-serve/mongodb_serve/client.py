import os
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure


_client: Optional[AsyncIOMotorClient] = None


def get_client() -> AsyncIOMotorClient:
    """
    Returns a singleton MongoDB Async client.
    Uses MongoDB Atlas connection string via MONGODB_URI.
    """
    global _client

    if _client is None:
        mongo_uri = os.getenv("MONGODB_URI")
        if not mongo_uri:
            raise RuntimeError("MONGODB_URI is not set")

        # For mongodb+srv URIs, SSL is automatically enabled
        # Remove conflicting SSL parameters and let the URI handle SSL
        _client = AsyncIOMotorClient(
            mongo_uri,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=20000,
            socketTimeoutMS=20000,
        )

    return _client


def get_database():
    """
    Returns the configured MongoDB database.
    """
    db_name = os.getenv("MONGODB_DB_NAME", "ghargpt")
    return get_client()[db_name]


async def ping() -> bool:
    """
    Health check to verify MongoDB connectivity.
    """
    try:
        await get_client().admin.command("ping")
        return True
    except ConnectionFailure:
        return False
