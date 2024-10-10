"""Initial migration

Revision ID: 4da6ee467006
Revises: 
Create Date: 2024-10-07 23:07:06.604064

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


# revision identifiers, used by Alembic.
revision: str = '4da6ee467006'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Bind to the current database connection
    connection = op.get_bind()
    inspector = inspect(connection)

    # Check if the 'alembic_version' table already exists
    if not inspector.has_table('alembic_version'):
        # Create the 'alembic_version' table
        op.create_table(
            'alembic_version',
            sa.Column('version_num', sa.String(length=32), nullable=False),
        )
        op.execute('INSERT INTO alembic_version (version_num) VALUES ("{}")'.format(revision))
    else:
        print("Table 'alembic_version' already exists. Skipping creation.")



    # Check if the 'qa' table already exists
    if not inspector.has_table('qa'):
        # Create the 'qa' table with created_at and updated_at columns
        op.create_table(
            'qa',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('question', sa.String, nullable=False),
            sa.Column('answer', sa.String, nullable=False),
            sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False),
            sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        )
    else:
        print("Table 'qa' already exists. Skipping creation.")

def downgrade():
    op.drop_table('qa')
