from sqlalchemy import (
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


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

    def __str__(self) -> str:
        return self.name
