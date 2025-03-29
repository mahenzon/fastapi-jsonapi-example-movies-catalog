"""create genre table

Revision ID: 22b171e7911e
Revises: 96530a77d45f
Create Date: 2025-03-29 20:24:29.182425

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "22b171e7911e"
down_revision: Union[str, None] = "96530a77d45f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION citext;")
    op.create_table(
        "genres",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column(
            "name",
            postgresql.CITEXT(length=20),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_genres"),
        ),
        sa.UniqueConstraint(
            "name",
            name=op.f("uq_genres_name"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("genres")
    op.execute("DROP EXTENSION citext;")
