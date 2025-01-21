from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DisplayWord(BaseModel):
    id: UUID
    ru: str
    en: str
    level: int
    topic_id: UUID

    model_config = ConfigDict(from_attributes=True)


class CreateWord(BaseModel):
    ru: str
    en: str
    level: int
    topic_id: UUID


class UpdateWord(BaseModel):
    ru: str | None = None
    en: str | None = None
    level: int | None = None
    topic_id: UUID | None = None
