from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from redis.asyncio import Redis


class Settings(BaseSettings):
    DB_NAME: str = Field("postgres")
    DB_HOST: str = Field("localhost")
    DB_PORT: str = Field("5432")
    DB_USER: str = Field("postgres")
    DB_PASS: str = Field("postgres")

    redis: Redis | None = Field(default=None, init=False)
    REDIS_HOST: str = Field("localhost")
    REDIS_PORT: str = Field("6379")

    model_config = SettingsConfigDict(env_file="conf/.env", env_file_encoding="utf-8")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.redis = Redis(host=self.REDIS_HOST, port=self.REDIS_PORT, decode_responses=True)

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
