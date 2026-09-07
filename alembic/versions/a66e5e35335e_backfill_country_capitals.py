"""backfill country capitals

Revision ID: a66e5e35335e
Revises: 30c13b3ec001
Create Date: 2026-09-07 22:29:23.756878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a66e5e35335e'
down_revision: Union[str, Sequence[str], None] = '30c13b3ec001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
    "UPDATE countries SET capital = 'Jakarta' WHERE name = 'Indonesia'"
)
    op.execute(
    "UPDATE countries SET capital = 'Monaco' WHERE name = 'Monaco'"
)
    op.execute(
    "UPDATE countries SET capital = 'Warsaw' WHERE name = 'Poland'"
)


def downgrade() -> None:
    op.execute(
    "UPDATE countries SET capital = 'Unknown' "
    "WHERE name in ('Indonesia', 'Monaco', 'Poland')"
)
