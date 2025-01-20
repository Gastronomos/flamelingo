from redis.asyncio import Redis

from api.src.settings import settings

redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)
