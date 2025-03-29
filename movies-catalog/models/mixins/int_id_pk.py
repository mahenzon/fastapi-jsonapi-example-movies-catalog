from sqlalchemy import Identity, Integer
from sqlalchemy.orm import Mapped, mapped_column


class IntIdPk:
    id: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
    )
