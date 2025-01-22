import contextlib

from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users.authentication import CookieTransport
from redis import Redis
from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AdminConfig, AdminUser, AuthProvider
from starlette_admin.exceptions import LoginFailed

from api.src.auth.manager import get_user_manager
from api.src.constants import COOKIE_NAME
from api.src.controllers.users import fastapi_users
from api.src.dao.users import UsersDAO
from api.src.db.config import get_async_session
from api.src.db.models import get_user_db
from api.src.db.s3 import media_url
from api.src.settings import settings

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


class UsernameAndPasswordProvider(AuthProvider):
    """
    This is only for demo purpose, it's not a better
    way to save and validate user credentials
    """

    def __init__(self, login_path="/login", logout_path="/logout", allow_paths=None, allow_routes=None):
        super().__init__(login_path, logout_path, allow_paths, allow_routes)
        self.backend = fastapi_users.authenticator.backends[0]
        self.strategy = fastapi_users.authenticator.backends[0].get_strategy()
        self.transport = fastapi_users.authenticator.backends[0].transport

    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.authenticate(OAuth2PasswordRequestForm(username=username, password=password))
                    if user:
                        r = await self.backend.login(self.strategy, user)
                        if isinstance(self.transport, CookieTransport):
                            response.set_cookie(
                                self.transport.cookie_name,
                                r.headers.get("set-cookie").split(";")[0].split("=")[1],
                                max_age=self.transport.cookie_max_age,
                                path="/",
                                domain=self.transport.cookie_domain,
                                secure=self.transport.cookie_secure,
                                httponly=self.transport.cookie_httponly,
                                samesite=self.transport.cookie_samesite,
                            )
                        else:
                            raise NotImplementedError("Only CookieTransport is supported")
                        return response

                    else:
                        raise LoginFailed("Invalid username or password")

    async def is_authenticated(self, request) -> bool:
        session_id = request.cookies.get(COOKIE_NAME)
        if session_id:
            async with get_async_session_context() as session:
                async with get_user_db_context(session) as user_db:
                    async with get_user_manager_context(user_db) as user_manager:
                        user = await self.strategy.read_token(session_id, user_manager)
                        return user is not None
        return False

    def get_admin_config(self, request: Request) -> AdminConfig:
        return AdminConfig(
            app_title="Admin panel",
        )

    def get_admin_user(self, request: Request) -> AdminUser:
        user_id = Redis(settings.REDIS_HOST, settings.REDIS_PORT, decode_responses=True).get(
            self.strategy.key_prefix + request.cookies.get(COOKIE_NAME)
        )
        user = UsersDAO.find_by_id_sync(user_id)
        return AdminUser(username=user.username, photo_url=request.url_for("files", path=media_url(user.avatar_id)))

    async def logout(self, request: Request, response: Response) -> Response:
        response.delete_cookie(COOKIE_NAME)
        return response
