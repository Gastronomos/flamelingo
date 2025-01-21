from uuid import UUID

from pydantic import BaseModel, ConfigDict

from api.src.schemas.base import Pagination


class DisplayWord(BaseModel):
    id: UUID
    ru: str
    en: str
    level: int
    part_of_speech: str
    topic_id: UUID

    model_config = ConfigDict(from_attributes=True)


class CreateWord(BaseModel):
    ru: str
    en: str
    level: int
    part_of_speech: str
    topic_id: UUID


class UpdateWord(BaseModel):
    ru: str | None = None
    en: str | None = None
    level: int | None = None
    part_of_speech: str | None = None
    topic_id: UUID | None = None


class SearchWord(Pagination):
    ru: str | None = None
    en: str | None = None
    level: int | None = None
    part_of_speech: str | None = None
    topic_id: UUID | None = None
