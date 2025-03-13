# k8s refresher

This is a simple API written in Python (FastAPI) and deployed to a local Kubernetes cluster (Minikube).

## API Development

The API is a sample FastAPI application. To work with this app, first `cd` into the `/api` directory.

```bash
cd api
```

### Activate the Python virtual environment

```bash
source .venv/bin/activate
```

### Installing dependencies

```bash
pip install <package>
```

### Run locally

```bash
fastapi dev src/app.py
```

## Build

### Building the API server

First, install Colima:

```bash
brew install colima
```

Start Docker:

```bash
colima start
```

Next, build the container:

```bash
cd api
docker build -t api:v1 .
```

## Production

### Run API

Run locally:

```bash
cd api
fastapi run src/app.py
```

Or, run from Docker. First, start docker, follow the above build instructions, and start the container:

```bash
docker run --name api api:v1 -p 8000:8000
```