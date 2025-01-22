from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session, selectinload

from api.src.db.config import async_session, sync_engine


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
            for instance in instances:
                await session.refresh(instance)
            return instances

    @classmethod
    async def update(cls, id, **data):
        data = {key: value for key, value in data.items() if value is not None}

        async with async_session() as session:
            query = (
                update(cls.model)
                .filter_by(id=id)
                .values(**data)
                .returning(cls.model)
                .execution_options(synchronize_session="fetch")
            )
            result = await session.execute(query)
            await session.commit()

            updated_instance = result.unique().scalar_one_or_none()
            if updated_instance:
                await session.refresh(updated_instance)
            return updated_instance

    @classmethod
    async def delete(cls, **data):
        async with async_session() as session:
            query = delete(cls.model).filter_by(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    def find_by_id_sync(cls, model_id):
        """Synchronous version of add method"""
        with Session(sync_engine) as session:
            return session.query(cls.model).filter_by(id=model_id).first()
