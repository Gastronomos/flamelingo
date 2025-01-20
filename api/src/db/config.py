from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from api.src.settings import settings

async_engine = create_async_engine(
    settings.database_url,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=300,
)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
