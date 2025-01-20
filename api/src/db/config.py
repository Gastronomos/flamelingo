from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from api.src.settings import settings

async_engine = create_async_engine(
    settings.database_url,
    echo=True,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=300,
)
async_session = async_sessionmaker(async_engine)
