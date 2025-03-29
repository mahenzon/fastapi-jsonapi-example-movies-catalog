from fastapi_jsonapi.schema_base import BaseModel
from pydantic import constr


class GenreBaseSchema(BaseModel):
    name: constr(
        min_length=1,
        max_length=20,
        to_lower=True,
    )
    description: str


class GenreCreateSchema(GenreBaseSchema):
    """
    Create
    """


class GenreUpdateSchema(GenreBaseSchema):
    description: str | None = None


class GenreSchema(GenreBaseSchema):
    name: str
