from beanie import Document
from pydantic import EmailStr

class User(Document):
    name: str
    email: EmailStr
    role: str = "user"
    is_active: bool = True

    class Settings:
        name = "users"