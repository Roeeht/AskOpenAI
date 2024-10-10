# Flask App with PostgreSQL and OpenAI Integration

This project is a Flask web app that integrates with PostgreSQL for data storage and OpenAI for processing questions. It is containerized using Docker.

## Setup Instructions

### Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- OpenAI API Key

### Environment Setup

1. **Clone the Repository**:
    ```bash
   git clone https://github.com/roeeht/AskOpenAI.git
   cd AskOpenAI
    ```
### Create the `.env` File:

2. Update the `.env.example` file with your database credentials and OpenAI API key:

    ```bash
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_DB=your_db_name
    SQLALCHEMY_DATABASE_URI=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
    OPENAI_API_KEY=your_openai_api_key
    FLASK_PORT=your_flask_port
    DB_PORT=your_db_port
    ```

2. Run the following command to copy the example file to `.env`:

    ```bash
    cp .env.example .env
    ```


### Run the Application

1. **Build and Run the Containers**:
    ```bash
   docker-compose up --build
   ```
    This will start both the Flask app and the PostgreSQL database in Docker containers.
    

### Useful Docker Commands

- **Start the app**:
  ```bash
  docker-compose up
  ```
- **Stop the app**:
  ```bash
  docker-compose down
  ```
- **Rebuild the containers**:
  ```bash
  docker-compose up --build
  ```
- **Check logs**:
  ```bash
  docker-compose logs web # Flask app logs
  docker-compose logs db # PostgreSQL logs
  ```
### Accessing the Application

- Flask Web App: The Flask app will be running at http://localhost:5000.
- PostgreSQL Database: You can access the PostgreSQL database through the following command:
  docker exec -it <db-container-name> psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}
  Replace <db-container-name> with the name of the PostgreSQL container.

### Testing :

To run the tests use the test service:
```bash
docker-compose run test
```
