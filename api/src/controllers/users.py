from uuid import UUID

from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from api.src.auth.manager import get_user_manager
from api.src.auth.oauth import enabled_providers
from api.src.auth.transport import auth_backend
from api.src.db.models import Users
from api.src.schemas.users import CreateUser, DisplayUser, UpdateUser
from api.src.settings import settings

router = APIRouter(tags=["users"], prefix="/users")


fastapi_users = FastAPIUsers[Users, UUID](
    get_user_manager,
    [auth_backend],
)

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

# TODO: redo
router.include_router(fastapi_users.get_users_router(DisplayUser, UpdateUser, requires_verification=True))
