from datetime import date
from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel

title_constrained = Annotated[
    str,
    MinLen(1),
    MaxLen(120),
]


class MovieBaseSchema(BaseModel):
    title: str
    description: str
    release_date: date | None = None
    duration: int | None = None
    age_rating: str | None = None


class MovieCreateSchema(MovieBaseSchema):
    """
    Create
    """

    title: title_constrained


class MovieUpdateSchema(MovieBaseSchema):
    title: title_constrained | None = None
    description: str | None = None
    release_date: date | None = None
    duration: int | None = None


class MovieSchema(MovieBaseSchema):
    id: int
