from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base

if TYPE_CHECKING:
    from models import Movie


class AgeRating(Base):
    name: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
    )
    description: Mapped[str] = mapped_column(
        Text(),
        default="",
        server_default="",
    )

    movies: Mapped[list["Movie"]] = relationship(
        back_populates="age_rating_obj",
    )

    def __str__(self) -> str:
        return self.name
