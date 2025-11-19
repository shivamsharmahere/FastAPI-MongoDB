from fastapi import APIRouter, HTTPException
from typing import List
from beanie import PydanticObjectId

from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate
from app.services import user_service

router = APIRouter()

@router.post("/users", response_model=User, status_code=201)
async def create_user_endpoint(user_input: UserCreate):
    # Check existing (simple logic can stay in routes, or move to service)
    existing = await User.find_one(User.email == user_input.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    return await user_service.create_user(user_input)

@router.get("/users", response_model=List[User])
async def get_all_users_endpoint():
    return await user_service.get_all_users()

@router.get("/users/{user_id}", response_model=User)
async def get_user_endpoint(user_id: PydanticObjectId):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/users/{user_id}", response_model=User)
async def update_user_endpoint(user_id: PydanticObjectId, data: UserUpdate):
    user = await user_service.update_user(user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}")
async def delete_user_endpoint(user_id: PydanticObjectId):
    success = await user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}