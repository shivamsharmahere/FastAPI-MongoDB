from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate
from beanie import PydanticObjectId
from typing import List, Optional

# The Service handles the Logic. It doesn't know about HTTP or HTML.

async def create_user(data: UserCreate) -> User:
    # Convert Schema -> Model
    user = User(name=data.name, email=data.email, role=data.role)
    await user.insert()
    return user

async def get_all_users() -> List[User]:
    return await User.find_all().to_list()

async def get_user(user_id: PydanticObjectId) -> Optional[User]:
    return await User.get(user_id)

async def update_user(user_id: PydanticObjectId, data: UserUpdate) -> Optional[User]:
    user = await User.get(user_id)
    if not user:
        return None
    
    # Update logic
    update_dict = data.dict(exclude_unset=True)
    await user.set(update_dict)
    return user

async def delete_user(user_id: PydanticObjectId) -> bool:
    user = await User.get(user_id)
    if not user:
        return False
    await user.delete()
    return True