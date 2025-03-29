from datetime import date
from typing import (
    TYPE_CHECKING,
    Annotated,
    Optional,
)

from annotated_types import MaxLen, MinLen
from fastapi_jsonapi.schema_base import BaseModel
from fastapi_jsonapi.types_metadata import RelationshipInfo

if TYPE_CHECKING:
    from schemas import AgeRatingSchema

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

    age_rating_obj: Annotated[
        Optional["AgeRatingSchema"],
        RelationshipInfo(
            resource_type="age-rating",
            resource_id_example="PG-13",
            id_field_name="name",
        ),
    ] = None


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
