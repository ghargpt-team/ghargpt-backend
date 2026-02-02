# apps/api/api/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from mongodb_serve.client import get_client, get_database, ping
from .properties import router as properties_router, init_property_service

# -------------------------------------------------------------------
# Load environment variables
# -------------------------------------------------------------------
load_dotenv(dotenv_path="../../.env")

# -------------------------------------------------------------------
# FastAPI App
# -------------------------------------------------------------------
app = FastAPI(title="GharGPT API")

# -------------------------------------------------------------------
# CORS Configuration
# -------------------------------------------------------------------
# Update / extend origins when needed
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://ghargpt.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],     # GET, POST, PUT, PATCH, DELETE, OPTIONS
    allow_headers=["*"],     # Authorization, Content-Type, etc.
)

# -------------------------------------------------------------------
# Database & Services
# -------------------------------------------------------------------
database = get_database()
init_property_service(database)

# -------------------------------------------------------------------
# Routers
# -------------------------------------------------------------------
app.include_router(properties_router)

# -------------------------------------------------------------------
# Health & Root Endpoints
# -------------------------------------------------------------------


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/health/db")
async def db_health():
    ok = await ping()
    return {"mongodb": "ok" if ok else "down"}

# -------------------------------------------------------------------
# Shutdown Handler
# -------------------------------------------------------------------


@app.on_event("shutdown")
def shutdown_db():
    client = get_client()
    client.close()
