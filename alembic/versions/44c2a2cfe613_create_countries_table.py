"""create countries table

Revision ID: 44c2a2cfe613
Revises: 
Create Date: 2026-05-21 09:54:20.744888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44c2a2cfe613'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
	"countries",
	sa.Column("id", sa.Integer(), primary_key=True),
	sa.Column("name", sa.String(), nullable=False),
	sa.Column("flag", sa.String(), nullable=False),
	sa.Column("difficulty", sa.String(), nullable=False),
	sa.Column("similar_to", sa.JSON(), nullable=False),
    )

def downgrade() -> None:
    op.drop_table("countries")
