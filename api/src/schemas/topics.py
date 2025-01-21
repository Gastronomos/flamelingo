from uuid import UUID

from pydantic import BaseModel, ConfigDict


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
