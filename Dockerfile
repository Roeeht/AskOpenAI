# Use the official Python image from Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies, including PostgreSQL client libraries
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*



# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make sure Alembic is installed
RUN pip install --no-cache-dir alembic


# Install testing dependencies like pytest
RUN pip install pytest pytest-mock

# Expose the Flask port
EXPOSE 5000

# Set the default environment variables
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
