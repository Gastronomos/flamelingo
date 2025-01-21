from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DisplayLevel(BaseModel):
    id: UUID
    stages: int
    topic_id: UUID

    model_config = ConfigDict(from_attributes=True)


class CreateLevel(BaseModel):
    stages: int
    topic_id: UUID


class UpdateLevel(BaseModel):
    stages: int | None = None
    topic_id: UUID | None = None
