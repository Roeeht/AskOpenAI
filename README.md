# Flask App with PostgreSQL and OpenAI Integration

This project is a Flask web app that integrates with PostgreSQL for data storage and OpenAI for processing questions. It is containerized using Docker.

## Setup Instructions

### Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- OpenAI API Key

### Environment Setup

1. **Clone the Repository**:
   git clone https://github.com/roeeht/AskOpenAI.git
   cd AskOpenAI

2. **Create the `.env` File**:
   -Update the `.env.example` file with your database credentials and OpenAI API key:
   POSTGRES_USER=your_db_user
   POSTGRES_PASSWORD=your_db_password
   POSTGRES_DB=your_db_name
   SQLALCHEMY_DATABASE_URI=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
   OPENAI_API_KEY=your_openai_api_key
   FLASK_PORT=your_flask_port
   DB_PORT=your_db_port
   -run:
   "cp .env.example .env"

### Run the Application

1. **Build and Run the Containers**:
   docker-compose up --build
   This will start both the Flask app and the PostgreSQL database in Docker containers.

2. **Access the App**:
   - Flask app: http://localhost:5000

### Useful Docker Commands

- **Start the app**:
  docker-compose up

- **Stop the app**:
  docker-compose down

- **Rebuild the containers**:
  docker-compose up --build

- **Check logs**:
  docker-compose logs web # Flask app logs
  docker-compose logs db # PostgreSQL logs

### Accessing the Application

- Flask Web App: The Flask app will be running at http://localhost:5000.
- PostgreSQL Database: You can access the PostgreSQL database through the following command:
  docker exec -it <db-container-name> psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}
  Replace <db-container-name> with the name of the PostgreSQL container.

### Testing the /ask Route:

To test the /ask route, run the tests using the test service:
docker-compose run test
