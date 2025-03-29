from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import (
    Date,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IntIdPk

if TYPE_CHECKING:
    from models import AgeRating


class Movie(IntIdPk, Base):
    title: Mapped[str] = mapped_column(
        String(120),
        index=True,
    )
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    release_date: Mapped[date | None] = mapped_column(
        Date,
    )
    duration: Mapped[int | None] = mapped_column(
        Integer,
    )
    age_rating: Mapped[str | None] = mapped_column(
        ForeignKey(
            "age_ratings.name",
            ondelete="SET NULL",
        ),
    )
    age_rating_obj: Mapped["AgeRating"] = relationship(
        back_populates="movies",
    )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Movie(id={self.id}, title={self.title!r})"
