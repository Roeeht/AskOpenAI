import os
import logging
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Alembic Config object
config = context.config

# Set up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# Load the database URL from environment variables, fallback to app config
database_url = os.getenv('SQLALCHEMY_DATABASE_URI')  # Load from .env or Docker environment
if not database_url:
    from app import app  # Only import Flask app if not in Docker environment
    database_url = app.config.get('SQLALCHEMY_DATABASE_URI')

# Set the database URL in Alembic config
config.set_main_option('sqlalchemy.url', database_url)

# Set the target metadata for 'autogenerate'
from models import db  # Import db and metadata from models
target_metadata = db.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
