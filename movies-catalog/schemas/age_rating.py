from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel

name_constrained = Annotated[
    str,
    MinLen(1),
    MaxLen(20),
]


class AgeRatingBaseSchema(BaseModel):
    name: str
    description: str


class AgeRatingCreateSchema(AgeRatingBaseSchema):
    name: name_constrained


class AgeRatingUpdateSchema(AgeRatingBaseSchema):
    name: name_constrained | None = None
    description: str | None = None


class AgeRatingSchema(AgeRatingBaseSchema):
    """
    Age Rating
    """
