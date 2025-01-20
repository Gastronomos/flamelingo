from typing import Optional
from uuid import UUID

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from api.src.db.models import Users, get_user_db
from api.src.settings import settings


class UserManager(UUIDIDMixin, BaseUserManager[Users, UUID]):
    reset_password_token_secret = settings.SESSION_SECRET
    verification_token_secret = settings.SESSION_SECRET

    async def on_after_register(self, user: Users, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_login(self, user, request=None, response=None):
        response.status_code = 301
        response.headers["Location"] = settings.BASE_URL

    async def on_after_forgot_password(self, user: Users, token: str, request: Optional[Request] = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: Users, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
