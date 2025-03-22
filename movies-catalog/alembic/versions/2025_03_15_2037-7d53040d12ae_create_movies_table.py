"""Create movies table

Revision ID: 7d53040d12ae
Revises:
Create Date: 2025-03-15 20:37:33.416842

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7d53040d12ae"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "movies",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("title", sa.String(length=120), nullable=False),
        sa.Column("description", sa.Text(), server_default="", nullable=False),
        sa.Column("release_date", sa.Date(), nullable=True),
        sa.Column("duration", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_movies")),
    )
    op.create_index(
        op.f("ix_movies_title"),
        "movies",
        ["title"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_movies_title"), table_name="movies")
    op.drop_table("movies")
