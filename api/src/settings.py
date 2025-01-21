from fastapi.templating import Jinja2Templates
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from redis.asyncio import Redis

from api.src.utils.email import Email


class Settings(BaseSettings):
    DEBUG: bool = True
    BASE_URL: str = "http://localhost:8000"

    DB_NAME: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"

    redis: Redis | None = Field(default=None, init=False)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: str = "6379"

    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_S3_BUCKET_NAME: str = ""
    AWS_S3_ENDPOINT_URL: str = ""
    AWS_S3_USE_SSL: bool = False
    AWS_DEFAULT_ACL: str = ""
    AWS_QUERYSTRING_AUTH: bool = False
    AWS_S3_CUSTOM_DOMAIN: str = ""

    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    LINKEDIN_CLIENT_ID: str = ""
    LINKEDIN_CLIENT_SECRET: str = ""
    MICROSOFT_CLIENT_ID: str = ""
    MICROSOFT_CLIENT_SECRET: str = ""

    SESSION_SECRET: str = "test_secret"

    SMTP_HOST: str = ""
    SMTP_PORT: str = ""
    SMTP_EMAIL: str = ""
    SMTP_PASSWORD: str = ""
    email: Email | None = Field(default=None, init=False)

    templates: Jinja2Templates = Jinja2Templates(directory="api/templates")

    model_config = SettingsConfigDict(env_file="conf/.env", env_file_encoding="utf-8")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.redis = Redis(host=self.REDIS_HOST, port=self.REDIS_PORT, decode_responses=True)
        self.email = Email(self.SMTP_HOST, self.SMTP_PORT, self.SMTP_EMAIL, self.SMTP_PASSWORD, self.SMTP_EMAIL)

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
