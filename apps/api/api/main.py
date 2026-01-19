# apps/api/api/main.py
from fastapi import FastAPI
from dotenv import load_dotenv
from mongodb_serve.client import get_client, get_database
from mongodb_serve.client import ping
from .properties import router as properties_router, init_property_service

# Load environment variables from project root
load_dotenv(dotenv_path="../../.env")

app = FastAPI(title="GharGPT API")

# Initialize database and services
database = get_database()
init_property_service(database)

# Include routers
app.include_router(properties_router)


@app.get("/health/db")
async def db_health():
    ok = await ping()
    return {"mongodb": "ok" if ok else "down"}


@app.get("/")
def root():
    return {"status": "ok"}


@app.on_event("shutdown")
def shutdown_db():
    client = get_client()
    client.close()
