from fastapi import FastAPI
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import certifi

# IMPORTS from our modular folders
from app.core.config import settings
from app.models.user_model import User
from app.api import user_routes

# 1. THE LIFESPAN (Connection Logic)
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting up...")
    
    # A. Connect to Motor
    client = AsyncIOMotorClient(settings.MONGO_URL, tlsCAFile=certifi.where())
    
    # B. Initialize Beanie
    # We must specify the database name here (e.g., 'test_db' or get from URL)
    # Accessing the default database from the connection string:
    db = client[settings.MONGO_DB_NAME]
    
    await init_beanie(database=db, document_models=[User])
    
    print("✅ Database Connected!")
    yield
    print("🛑 Shutting down...")

# 2. THE APP DEFINITION
app = FastAPI(title="Modular User API", lifespan=lifespan)

# 3. REGISTER ROUTERS
app.include_router(user_routes.router)