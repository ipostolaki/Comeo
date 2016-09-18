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

celery -A comeo_project worker -l info --logfile=/var/log/celery.log