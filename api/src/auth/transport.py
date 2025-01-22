from fastapi_users.authentication import AuthenticationBackend, CookieTransport, RedisStrategy

from api.src.constants import COOKIE_MAX_AGE, COOKIE_NAME
from api.src.db.redis import redis

cookie_transport = CookieTransport(
    cookie_name=COOKIE_NAME, cookie_max_age=COOKIE_MAX_AGE, cookie_path="/", cookie_samesite="none"
)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=COOKIE_MAX_AGE)


auth_backend = AuthenticationBackend(
    name="cookie_auth",
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)
