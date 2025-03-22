from datetime import date

from sqlalchemy import (
    Date,
    Identity,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Movie(Base):
    id: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
        autoincrement=True,
    )
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
    # TODO: age rating relation

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Movie(id={self.id}, title={self.title!r})"
