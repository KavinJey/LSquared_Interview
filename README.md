# lsquared_interview

Create API from where the user can select from availabile images, select a time range, and assign this to the device(s).

Routes:

```(python)
'http://localhost:8000/api/v1/images/' # GET for images
'http://localhost:8000/api/v1/devices/' # GET for devices
'http://localhost:8000/api/v1/content' # POST for content
```

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

OR

- Pipenv
- Pip

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

To seed the db with devices use the command

```bash
python manage.py seed
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
