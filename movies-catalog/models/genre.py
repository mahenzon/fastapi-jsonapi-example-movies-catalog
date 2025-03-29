from sqlalchemy import (
    Text,
)
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from models.base import Base
from models.mixins import IntIdPk


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

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (
            f"Genre(id={self.id}, name={self.name!r}, description={self.description!r})"
        )
