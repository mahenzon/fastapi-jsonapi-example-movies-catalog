from sqlalchemy import (
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from models.base import Base
from models.mixins import IntIdPk


class MovieGenre(IntIdPk, Base):
    __tablename__ = "movie_genre_association"

    movie_id: Mapped[int] = mapped_column(
        ForeignKey(
            "movies.id",
            ondelete="CASCADE",
        ),
    )
    genre_id: Mapped[int] = mapped_column(
        ForeignKey(
            "genres.id",
            ondelete="CASCADE",
        ),
    )

    __table_args__ = (
        UniqueConstraint(
            movie_id,
            genre_id,
        ),
    )
