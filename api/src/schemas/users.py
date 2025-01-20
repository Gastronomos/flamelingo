from datetime import datetime
from uuid import UUID

from fastapi_users import schemas
from pydantic import ConfigDict, EmailStr


class DisplayUser(schemas.BaseUser[UUID]):
    id: UUID
    email: EmailStr
    username: str
    avatar_id: str | None
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateUser(schemas.BaseUserCreate):
    email: EmailStr
    password: str


class UpdateUser(schemas.BaseUserUpdate):
    username: str | None = None
    avatar_id: str | None = None
