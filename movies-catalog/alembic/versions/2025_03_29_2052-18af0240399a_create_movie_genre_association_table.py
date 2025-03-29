"""create movie_genre_association table

Revision ID: 18af0240399a
Revises: 22b171e7911e
Create Date: 2025-03-29 20:52:18.007429

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "18af0240399a"
down_revision: Union[str, None] = "22b171e7911e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "movie_genre_association",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column(
            "movie_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "genre_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["genre_id"],
            ["genres.id"],
            name=op.f("fk_movie_genre_association_genre_id_genres"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movies.id"],
            name=op.f("fk_movie_genre_association_movie_id_movies"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_movie_genre_association"),
        ),
        sa.UniqueConstraint(
            "movie_id",
            "genre_id",
            name=op.f("uq_movie_genre_association_movie_id_genre_id"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("movie_genre_association")
