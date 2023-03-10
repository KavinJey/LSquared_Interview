# lsquared_interview

Create API from where the user can select from availabile images, select a time range, and assign this to the device(s).

Routes:

```(python)
http://localhost:8000/api/v1/images/ # GET for images
http://localhost:8000/api/v1/devices/ # GET for devices
http://localhost:8000/api/v1/content # POST for content
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

`/lsquared/content/views.py`

- API Views are located here

`/lsquared/content/models.py`

- DB models are declared here

`/lsquared/content/serializers.py`

- serializers for models written here

`/lsquared/content/assets`

- Folder which houses the images that are served

`/lsquared/content/json`

- Folder which houses device json (auto generated by API)
