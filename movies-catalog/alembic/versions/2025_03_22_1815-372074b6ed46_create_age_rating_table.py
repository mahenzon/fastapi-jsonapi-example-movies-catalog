"""create age rating table

Revision ID: 372074b6ed46
Revises: 7d53040d12ae
Create Date: 2025-03-22 18:15:48.351936

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "372074b6ed46"
down_revision: Union[str, None] = "7d53040d12ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "age_ratings",
        sa.Column(
            "name",
            sa.String(length=20),
            sa.Identity(always=False),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "name",
            name=op.f("pk_age_ratings"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("age_ratings")
