from sqlalchemy import delete, select
from sqlalchemy.orm import selectinload

from api.src.db.config import async_session


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, offset: int | None = None, limit: int | None = None, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by).options(selectinload("*")).offset(offset).limit(limit)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add(cls, **data):
        async with async_session() as session:
            instance = cls.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    @classmethod
    async def add_all(cls, rows: list[dict]):
        async with async_session() as session:
            instances = [cls.model(**row) for row in rows]
            session.add_all(instances)
            await session.commit()
            await session.refresh(instances)
            return instances.scalars().all()

    @classmethod
    async def delete(cls, **data):
        async with async_session() as session:
            query = delete(cls.model).filter_by(**data)
            await session.execute(query)
            await session.commit()
