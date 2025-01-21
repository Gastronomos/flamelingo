import secrets
from typing import Optional
from uuid import UUID

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from api.src.constants import CODE_MAX_AGE
from api.src.db.models import Users, get_user_db
from api.src.db.redis import redis
from api.src.settings import settings
from api.src.tasks.tasks import verification_flow


class UserManager(UUIDIDMixin, BaseUserManager[Users, UUID]):
    reset_password_token_secret = settings.SESSION_SECRET
    verification_token_secret = settings.SESSION_SECRET

    async def on_after_login(self, user, request=None, response=None):
        if not str(request.url).endswith("/login"):
            response.status_code = 301
            response.headers["Location"] = settings.BASE_URL

    async def on_after_forgot_password(self, user: Users, token: str, request: Optional[Request] = None):
        code = str(secrets.randbelow(1000000)).zfill(6)
        await redis.setex(code, CODE_MAX_AGE, token)
        verification_flow.delay(code, user.to_dict(), "change_password", "reset_password.html")

    async def on_after_request_verify(self, user: Users, token: str, request: Optional[Request] = None):
        code = str(secrets.randbelow(1000000)).zfill(6)
        await redis.setex(code, CODE_MAX_AGE, token)
        verification_flow.delay(code, user.to_dict(), "verify", "verify_email.html")

    async def reset_password(self, token, password, request=None):
        return await super().reset_password(await redis.get(token), password, request)

    async def verify(self, token, request=None):
        return await super().verify(await redis.get(token), request)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
