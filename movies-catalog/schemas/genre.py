from typing import TYPE_CHECKING, Annotated, Optional

from fastapi_jsonapi.schema_base import BaseModel
from fastapi_jsonapi.types_metadata import RelationshipInfo
from pydantic import constr

if TYPE_CHECKING:
    from schemas import MovieSchema


class GenreBaseSchema(BaseModel):
    name: constr(
        min_length=1,
        max_length=20,
        to_lower=True,
    )
    description: str

    movies: Annotated[
        Optional[list["MovieSchema"]],
        RelationshipInfo(
            resource_type="movie",
            many=True,
        ),
    ] = None


class GenreCreateSchema(GenreBaseSchema):
    """
    Create
    """


class GenreUpdateSchema(GenreBaseSchema):
    description: str | None = None


class GenreSchema(GenreBaseSchema):
    name: str
