from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel


class AgeRatingBaseSchema(BaseModel):
    description: str


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
