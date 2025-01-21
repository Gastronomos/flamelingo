from uuid import UUID

from pydantic import BaseModel, ConfigDict

from api.src.schemas.base import Pagination


class DisplayTopic(BaseModel):
    id: UUID
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)


class CreateTopic(BaseModel):
    name: str
    description: str


class UpdateTopic(BaseModel):
    name: str | None = None
    description: str | None = None


class SearchTopic(Pagination):
    name: str | None = None
