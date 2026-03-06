"""change default price value

Revision ID: 367b5eef4670
Revises: 28ac9c23c96e
Create Date: 2026-03-06 18:57:59.005789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '367b5eef4670'
down_revision: Union[str, Sequence[str], None] = '28ac9c23c96e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "stocks",
        "price",
        server_default="0.00"
    )


def downgrade() -> None:
    op.alter_column(
        "stocks",
        "price",
        server_default=None
    )
