"""add age_rating col to movies

Revision ID: 96530a77d45f
Revises: 372074b6ed46
Create Date: 2025-03-22 20:26:06.771410

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "96530a77d45f"
down_revision: Union[str, None] = "372074b6ed46"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "movies",
        sa.Column(
            "age_rating",
            sa.String(length=20),
            nullable=True,
        ),
    )
    op.create_foreign_key(
        op.f("fk_movies_age_rating_age_ratings"),
        "movies",
        "age_ratings",
        ["age_rating"],
        ["name"],
        ondelete="SET NULL",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        op.f("fk_movies_age_rating_age_ratings"),
        "movies",
        type_="foreignkey",
    )
    op.drop_column("movies", "age_rating")
