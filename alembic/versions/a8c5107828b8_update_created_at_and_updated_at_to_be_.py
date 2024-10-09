"""Update created_at and updated_at to be nullable

Revision ID: a8c5107828b8
Revises: 4da6ee467006
Create Date: 2024-10-08 09:42:57.819570

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a8c5107828b8'
down_revision: Union[str, None] = '4da6ee467006'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.alter_column('qa', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('qa', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)

def downgrade() -> None:
    op.alter_column('qa', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('qa', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
