"""Add Capital field to countries

Revision ID: 30c13b3ec001
Revises: c25af52a672b
Create Date: 2026-05-26 13:23:04.384951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30c13b3ec001'
down_revision: Union[str, Sequence[str], None] = 'c25af52a672b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "countries",
        sa.Column("capital", sa.String(), nullable=True)
    )

    op.execute("UPDATE countries SET capital = 'Unknown' WHERE capital IS NULL")

    op.alter_column(
        "countries",
        "capital",
        nullable=False
    )


def downgrade() -> None:
    op.drop_column("countries", "capital")
