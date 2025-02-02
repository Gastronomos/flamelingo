from uuid import UUID

from pydantic import BaseModel, ConfigDict

from api.src.schemas.base import Pagination


class DisplayRule(BaseModel):
    id: UUID
    name: str
    description: str
    topic_id: UUID

    model_config = ConfigDict(from_attributes=True)


class CreateRule(BaseModel):
    name: str
    description: str
    topic_id: UUID


class UpdateRule(BaseModel):
    name: str | None = None
    description: str | None = None
    topic_id: UUID | None = None


class SearchRule(Pagination):
    name: str | None = None
    topic_id: UUID | None = None
