from pydantic import BaseModel


class Pagination(BaseModel):
    limit: int | None = 50
    offset: int | None = 0
