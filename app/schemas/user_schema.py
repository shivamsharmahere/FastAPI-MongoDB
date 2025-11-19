from pydantic import BaseModel, EmailStr
from typing import Optional

# INPUT Schema (What the user sends us)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: str

# UPDATE Schema (What the user sends to update)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None