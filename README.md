# FastApi MongoDB Project-Template Example

## description

This template can be used as base project template if rest-api with mongo db is required. The template shows how to manage students using the rest api & mongo db. For authentication and API access the oauth2 password flow with bearer token is used.

---

## project structure

- src (python code)
  - auth (auth admin user, jwt handling)
  - config (app configs based on .env file)
  - database (mongo db access)
  - models (data models)
  - routes (api endpoints)
  - test (postman collection, unit tests)
  - Dockerfile (dockerfile for image)
  - main(.py) (entry point for app)
  - requirements(.txt) (python dependencies)
- docker-compose(.yml) (container configuration and initalitation to serve complete app)
- README (project description)

---

## Config

- `.env.example` file in config folder shows example for `.env` file
- modify example file to your needs and change file name to .env
- `.env` file will not be commited to your repo

## API access

- api uses oauth2 password schema
- get access token (bearer) via token route with username and password
- actual only admin user
  - inital `username: admin`
  - inital `password: admin`
- can be changed in `.env`
- password has to encrypt with bcrypt to save only hash in `.env`

---

## run app

Deployment is docker based. Execute the commands on the same folder level where the docker-compose file is located.

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

- refactor auth and jwt code -> classed based
  - config if username & password is needed or other auth methods (only api key)
  - refactor admin access
- add unit tests
- API Doc -> response definition for each endpoint (404 not for each endpoint necessary)
- docker-compose -> plain user & pw -> use from env file
- add https
- add logging -> debug & error Log
- add cors config to .env file -> config, not hard coded
- do not expose database ID's -> create UUID's and use them
- models / routes change folder structure -> base & specific
  - for new use cases only specific folders has to be changed
