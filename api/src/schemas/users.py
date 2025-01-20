from datetime import datetime

from pydantic import BaseModel


class DisplayUser(BaseModel):
    id: int
    user_id: int
    sso_type: int
    username: str
    avatar: str
    email: str
    is_admin: bool
    is_enabled: bool
    created_at: datetime
