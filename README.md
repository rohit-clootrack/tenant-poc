# Tenant Management

Behold My Awesome Microservice Project!

### Folder Structure
```
.
├── Dockerfile
├── README.md
├── TODO.md
├── dapr.yaml
├── db.sqlite3
├── tenant_management
│   ├── __init__.py
│   ├── app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── config.py
│   │   ├── controllers
│   │   │   ├── __init__.py
│   │   │   └── tenant.py
│   │   ├── db_interface
│   │   │   ├── __init__.py
│   │   │   └── tenant.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── tenant.py
│   │   ├── serializers
│   │   │   ├── __init__.py
│   │   │   └── tenant.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── tenant.py
│   │   └── utils
│   │       ├── __init__.py
│   │       └── errors.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── local.yml
├── manage.py
├── pyproject.toml
├── requirements.txt
└── setup.cfg
```
### Features
* RESTful APIs
* Standard Error message
* Unit Tests
* Pre-commit hooks
* OpenAPI schema / Swagger
* Pagination -- Limit Offset Count
* Continuous Integration - GitHub Actions

### Endpoints
* GET `/api/v1.0/tenants`
* POST `/api/v1.0/tenants`
* GET `/api/v1.0/tenants/:id`
* PUT `/api/v1.0/tenants/:id`
* DELETE `/api/v1.0/tenants/:id`

## Basic Commands

### Create virtual environment and install dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Migrations
Copy the sample env file and make changes as per the environment
```
cp .env.sample .env
```

Make changes models.py to suit the needs of your app

Generate migration files using the following command
```
python3 manage.py makemigrations
```

Run the migration
```
python3 manage.py migrate
```

### Setting Up Your Users

To create a **superuser account**, use this command:

```
python3 manage.py createsuperuser
```

### Run Server
```
python3 manage.py runserver 8000
```

### Pre-Commit Hooks
Install pre-commit hook using the following command. After this, pre-commit hooks will be executed everytime you commit the code.
```
pre-commit install
```

Incase, you want to manually trigger the pre-commit hooks
```
pre-commit run all-files
```
### Type checks

Running type checks with mypy:
```
mypy tenant_management/app
```

#### Running tests with Pytest

```
python3 manage.py test tenant_management.app.tests.tenant
```

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```commandline

coverage run -m pytest
coverage html
open htmlcov/index.html
```

> Notes of naming stuff:
* Name Mold : [adjective]_[noun]_[measurement]
  * Example: Suppose you are storing maximum number of order per month. What is the variable name?
    * max_order_length

    [Learn More](https://www.youtube.com/watch?v=z7w2lKG8zWM&t=325s)

### DAPR
#### Installation

```
brew install dapr/tap/dapr-cli
dapr init
```
#### Standalone Mode
```
dapr run --app-id tenant_app --app-port 8000 --dapr-http-port 3500 python3 manage.py runserver 8000

```
Make a request:
```commandline
curl http://localhost:3500/v1.0/invoke/tenant_app/method/api/v1.0/tenants/
```

#### Kubernetes

* Build Docker Image
```
docker build . -t neo_tenant_management:latest
```

* Run docker-compose
```
 docker-compose -f local.yml up --build
```
[This section is under construction]

### API References

#### Sample Paginated Response
```json
{
    "count": 2,
    "next": "http://localhost:8000/api/v1.0/tenants/?limit=1&offset=1",
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "test",
            "last_name": "asas",
            "email": "asas@gmail.com",
        }
    ]
}
```


#### Sample Error response
we are using `drf-standardized-errors` plugin for error response.

* **type** can be `client_error`, `server_error` or `validation_error`
```json
{
    "status": "error",
    "type": "client_error",
    "errors": [
        {
            "code": "not_found",
            "detail": "Not found.",
            "attr": null
        }
    ]
}
```


#### Swagger Documentation

* Swagger documentation is available at `/api/schema/swagger-ui/` endpoint
* Redoc documentation is available at `/api/schema/redoc/` endpoint
* OpenAPI schema is available at `/api/schema/openapi.json` endpoint
