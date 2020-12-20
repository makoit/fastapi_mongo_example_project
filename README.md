# FastApi MongoDB Project-Template

## description

This template can be used as base project template if rest-api with mongo db is required. Deployment is docker based.

---

## project structure

- src (python code)
  - auth (authentication with OAuth2PasswordBearer)
  - config (app configs)
  - database (mongo db access)
  - models (data models -> DTOs, DAOs)
  - routes (api endpoints)
  - test (postman collection, unit test)
  - utils (helper functions)
  - Dockerfile (dockerfile for image)
  - main(.py) (entry point for app)
  - requirements(.txt) (python dependencies)
- docker-compose(.yml) (container configuration and initalitation to serve complete app)
- README (project description)

---

## run app

Execute the commands on the same folder level where the docker-compose file is located.

### start app and mongo:

(run first time container are build, next time run this command container will not be build)

```sh
docker-compose up
```

### rebuild container:

```sh
docker-compose build --no-cache
```

### run after rebuild:

```sh
docker-compose down && docker-compose up
```

---

## API documentation

- Swagger Documentation find on http://localhost:8000/docs

---

## API access

- api uses oauth2 password schema
- get access token (bearer) via token route with username and password
- actual only admin user
  - inital username: admin
  - inital password: admin
- can be changed in config.yml
- password has to encrypt with bcrypt to save only hash in config.yml

---

## Static typing checks with mypy

[mypy](https://mypy.readthedocs.io/en/stable/index.html)

```sh
python -m mypy main.py
```

## important dependencies (libs)

- [fastapi](https://fastapi.tiangolo.com/)
- [motor](https://motor.readthedocs.io/en/stable/)
- [passlib](https://passlib.readthedocs.io/en/stable/)
- [jose](https://github.com/mpdavis/python-jose)

---

## to-do's

- add unit tests
- do not expose database ID's -> create UUID's and use them
- API Doc -> response definition for each endpoint (404 not for each endpoint necessary)
- app config and credentials non in plain text (env or hashed)
- add https
- add logging
