#!/usr/bin/env bash

# freeze what was installed during Dockerfile build,
# file will be saved to the docker-compose mounted volume
pip freeze > ./Docker/dev/requirements-freezed.txt

# run livereload server as bg job
python ./tools/live.py &

# Waiting for pg service is possible with official postgres docker image
# pg container start to listen to connections, only when setup/start process is complete
echo "Waiting for the database service..."
while ! nc -w 1 -z pg_database 5432;
do
  echo -n .
  sleep 1
done
echo "PostgresSQL database is ready"

python manage.py migrate  # apply migrations, if any

echo "Launching Django now"

echo "
  _|_|_|    _|_|    _|      _|  _|_|_|_|    _|_|
_|        _|    _|  _|_|  _|_|  _|        _|    _|
_|        _|    _|  _|  _|  _|  _|_|_|    _|    _|
_|        _|    _|  _|      _|  _|        _|    _|
  _|_|_|    _|_|    _|      _|  _|_|_|_|    _|_|
                                                    "
python manage.py runserver 0.0.0.0:80