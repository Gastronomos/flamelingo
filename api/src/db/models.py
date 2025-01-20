from datetime import datetime
from uuid import UUID, uuid4

from faker import Faker
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseOAuthAccountTableUUID, SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import UUID as GUID
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from api.src.db.config import get_async_session


class Base(DeclarativeBase):
    def to_dict(self):
        return {k: self.__dict__[k] for k in self.__dict__ if "_sa_" != k[:4]}

    def __repr__(self):
        return f"""<{self.__class__.__name__}({[', '.join('%s=%s' % (k, self.__dict__[k])
                                             for k in self.__dict__ if '_sa_' != k[:4])]}"""


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    id: Mapped[UUID] = mapped_column(GUID, primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(GUID, ForeignKey("user.id", ondelete="cascade"), nullable=False)


class Users(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(GUID, primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    avatar_id: Mapped[str | None] = mapped_column(String(length=320), default=None, nullable=True)
    hashed_password: Mapped[str | None] = mapped_column(String(length=1024), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = Column(DateTime, server_default=func.now(), nullable=False)

    oauth_accounts: Mapped[list[OAuthAccount]] = relationship("OAuthAccount", lazy="joined")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.username:
            fake = Faker()
            self.username = f"{fake.first_name()} {fake.last_name()}"


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, Users, OAuthAccount)
