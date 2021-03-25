#!/bin/sh
if [ -d "docker-compose" ]; then
    echo "docker-compose wasn't found"
else
    docker-compose rm
    echo "Creating .env file..."
    echo "PYTHON_PORT=8090
POSTGRES_DB=movies
POSTGRES_USER=movies
POSTGRES_PASSWORD=movies
DB_PORT=5434" > .env
    echo "Raising up containers..."
    docker-compose up
fi