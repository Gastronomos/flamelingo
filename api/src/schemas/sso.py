from pydantic import BaseModel


class CreateSSO(BaseModel):
    name: str
    client_id: str
    client_secret: str


class UpdateSSO(BaseModel):
    name: str
    client_id: str | None = None
    client_secret: str | None = None
