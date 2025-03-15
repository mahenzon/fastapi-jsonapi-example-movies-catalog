from datetime import date

from pydantic import BaseModel


class MovieBaseSchema(BaseModel):
    title: str
    description: str
    release_date: date | None = None
    duration: int | None = None


class MovieCreateSchema(MovieBaseSchema):
    """
    Create
    """


class MovieUpdateSchema(MovieBaseSchema):
    title: str | None = None
    description: str | None = None
    release_date: date | None = None
    duration: int | None = None


class MovieSchema(MovieBaseSchema):
    id: int
