from uuid import UUID

import httpx
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from fastapi.responses import RedirectResponse
from fastapi.testclient import TestClient
from fastapi_users import FastAPIUsers

from api.src.auth.manager import get_user_manager
from api.src.auth.oauth import enabled_providers
from api.src.auth.transport import auth_backend
from api.src.dao.users import UsersDAO
from api.src.db.models import Users
from api.src.db.s3 import file_storage
from api.src.schemas.users import CreateUser, DisplayUser, UpdateUser
from api.src.settings import settings

router = APIRouter(tags=["users"], prefix="/users")


fastapi_users = FastAPIUsers[Users, UUID](
    get_user_manager,
    [auth_backend],
)
get_current_active_user = fastapi_users.authenticator.current_user(active=True, verified=True)
get_current_superuser = fastapi_users.authenticator.current_user(active=True, verified=True, superuser=True)

router.include_router(fastapi_users.get_auth_router(auth_backend, requires_verification=True))

router.include_router(fastapi_users.get_register_router(DisplayUser, CreateUser))

router.include_router(fastapi_users.get_verify_router(DisplayUser))

router.include_router(fastapi_users.get_reset_password_router())

for provider in enabled_providers:
    router.include_router(
        fastapi_users.get_oauth_router(
            provider, auth_backend, settings.SESSION_SECRET, associate_by_email=True, is_verified_by_default=True
        ),
        prefix=f"/{provider.name}",
    )


@router.get("/me")
async def get_me(user: DisplayUser = Depends(get_current_active_user)) -> DisplayUser:
    return user


@router.patch("/me")
async def update_me(
    username: str | None = Form(None),
    avatar: UploadFile | None = File(None),
    password: str | None = Form(None),
    user: DisplayUser = Depends(get_current_active_user),
) -> DisplayUser:
    avatar_id = None
    if avatar:
        avatar_id = file_storage.write(avatar.file, avatar.filename)
    data = UpdateUser(username=username, avatar_id=avatar_id, password=password).model_dump()
    async for manager in get_user_manager():
        data["hashed_password"] = manager.password_helper.hash(password)
        data.pop("password")
    return await UsersDAO.update(user.id, **data)
