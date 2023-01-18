# lsquared_interview

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Local Development

Start the dev server for local development:

```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Alternative Local Development (w Pipenv)

```bash
pipenv install
python manage.py migrate
python manage.py runserver
```

# Files of Interest

- Note ASset folder
- Note views, serializers, etc

# Sql query

From user you receive
start_time
end_time

from table of start_time, end_time, id
find empty timeslots
