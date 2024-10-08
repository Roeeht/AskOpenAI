"""Initial migration

Revision ID: 4da6ee467006
Revises: 
Create Date: 2024-10-07 23:07:06.604064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4da6ee467006'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
from sqlalchemy import inspect

def upgrade():
    # Create the `qa` table
    op.create_table(
        'qa',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('question', sa.String, nullable=False),
        sa.Column('answer', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False)
    )

def downgrade():
    op.drop_table('qa')
