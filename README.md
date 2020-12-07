# FastApi MongoDB Project-Template

## description

This template can be used as base project template if rest-api with mongo db is required. Deployment is docker based.

---

## project structure

- src (python code)
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

## important dependencies (libs)

- [fastapi](https://fastapi.tiangolo.com/)
- [motor](https://motor.readthedocs.io/en/stable/)

---

## to-do's

- add unit tests
- add custom exceptions for db access -> exception handling chais
- update and integrate standard model for api response and error response
- add auth functionality with jwt
- app config and credentials non in plain text
- add https
