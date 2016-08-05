#!/usr/bin/env bash

# Waiting for pg service is possible with official postgres docker image
# pg container start to listen to connections, only when setup/start process is complete
echo "Waiting for the database service..."
while ! nc -w 1 -z pg_database 5432;
do
  echo -n .
  sleep 1
done
echo "PostgresSQL database is ready"


echo "Waiting for the neo service..."
while ! nc -w 1 -z neo 7474;
do
  echo -n .
  sleep 1
done
echo "Neo4j database is ready"

python manage.py migrate  # lab env should apply migrations(git pulled) before serving application
gunicorn --workers=2 --bind 0.0.0.0:80 comeo_project.wsgi:application