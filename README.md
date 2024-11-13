# RocketScience - Docker Challenge

This repository contains a simple Data Science application using Docker to simplify the setup and execution of environments. The application includes a Flask API, a machine learning model trained with `scikit-learn`, integration with the MySQL database, and MLFlow for model management. This project demonstrates how Docker can be used to isolate and orchestrate the necessary services for Data Science project development.

## Project Structure

The repository contains the following components:

- **Flask API**: A simple API service that allows training and making predictions with machine learning models.
- **MLFlow**: Used for registering and managing machine learning models.
- **MySQL Database**: Database for storing application logs (using SQLAlchemy for data manipulation).
- **Docker**: Used to containerize the application, MLFlow, and MariaDB.

## Directory Structure

```plaintext
.
├── api/
│   ├── app.py                  # Flask API code
│   ├── Dockerfile               # Dockerfile for the Flask service
│   ├── requirements.txt         # Flask dependencies
├── mlflow/
│   ├── Dockerfile               # Dockerfile for the MLFlow service
│   ├── mlflow_model/            # Trained models from MLFlow
├── database/
│   ├── init.sql                 # Script to create and configure the MariaDB database
│   ├── Dockerfile               # Dockerfile for the MariaDB service
├── docker-compose.yml           # Docker Compose file to orchestrate all services
├── logs/                        # Directory for storing application logs
├── utils/
│   └── params.py                # Configuration parameters
├── README.md                    # This file
└── requirements.txt             # Dependencies for running the project
```

## How to Run the Project

To run the project, you will need Docker and Docker Compose installed on your machine. Follow the steps below:

1. Clone the repository
```
git clone https://github.com/caiodearaujo/rs-dockerchallenge.git
cd rs-dockerchallenge
```

2. Build and start the containers
With Docker Compose, you can easily start all services:
```
docker-compose up build
```

3. Run only the API locally
Create a `.env` file inside the `/api` folder with the following variables:
```
MARIADB_HOST=localhost 
MLFLOW_TRACKING_URI=http://localhost:5001
```
Then run the command:
```
flask run --port 8080
```

4. Test the Endpoints
The API has the following endpoints:
 - POST /train: Trains a simple ML model with the Iris dataset.
 - GET /models: Returns the list of models trained in MLFlow.
 - GET /predict: Makes predictions using the trained model. You can provide a trained model ID, or if not provided, the latest model will be used.
 - GET /logs: Returns the logs stored in the MySQL database.
 - GET /ping: Returns `pong` to check the API health.

5. Stop the containers
To stop the containers, simply run the command:
```
docker-compose down
```