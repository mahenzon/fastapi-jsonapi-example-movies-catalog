__all__ = (
    "AgeRatingBaseSchema",
    "AgeRatingCreateSchema",
    "AgeRatingSchema",
    "AgeRatingUpdateSchema",
    "GenreBaseSchema",
    "GenreCreateSchema",
    "GenreSchema",
    "GenreUpdateSchema",
    "MovieBaseSchema",
    "MovieCreateSchema",
    "MovieSchema",
    "MovieUpdateSchema",
)

from .age_rating import (
    AgeRatingBaseSchema,
    AgeRatingCreateSchema,
    AgeRatingSchema,
    AgeRatingUpdateSchema,
)
from .genre import (
    GenreBaseSchema,
    GenreCreateSchema,
    GenreSchema,
    GenreUpdateSchema,
)
from .movie import (
    MovieBaseSchema,
    MovieCreateSchema,
    MovieSchema,
    MovieUpdateSchema,
)
