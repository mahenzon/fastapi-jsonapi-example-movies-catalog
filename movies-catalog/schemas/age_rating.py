from typing import (
    TYPE_CHECKING,
    Annotated,
    Optional,
)

from annotated_types import MaxLen, MinLen
from fastapi_jsonapi.schema_base import BaseModel
from fastapi_jsonapi.types_metadata import RelationshipInfo

if TYPE_CHECKING:
    from schemas import MovieSchema


class AgeRatingBaseSchema(BaseModel):
    description: str

    movies: Annotated[
        Optional[list["MovieSchema"]],
        RelationshipInfo(
            resource_type="movie",
            many=True,
        ),
    ] = None


class AgeRatingCreateSchema(AgeRatingBaseSchema):
    name: Annotated[
        str,
        MinLen(1),
        MaxLen(20),
    ]


class AgeRatingUpdateSchema(AgeRatingBaseSchema):
    description: str | None = None


class AgeRatingSchema(AgeRatingBaseSchema):
    name: str
