from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
)
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IntIdPk
from models.move_genre import MovieGenre

if TYPE_CHECKING:
    from models import Movie


class Genre(IntIdPk, Base):
    name: Mapped[str] = mapped_column(
        CITEXT(20),
        unique=True,
    )
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    movies: Mapped[set["Movie"]] = relationship(
        back_populates="genres",
        secondary=MovieGenre.__table__,
    )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (
            f"Genre(id={self.id}, name={self.name!r}, description={self.description!r})"
        )
