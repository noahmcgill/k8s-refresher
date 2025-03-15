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

## Deploy Kubernetes infrastructure via Minikube

I referred to [this article](https://devopscube.com/deploy-postgresql-statefulset/) for deploying a high-availability PostgreSQL service. To deploy the infrastructure, apply the following config files:

```bash
cd infra
kubectl apply -f postgres-config.yaml
kubectl apply -f postgres-svc.yaml
kubectl apply -f postgres-secret.yaml
kubectl apply -f postgres-statefulset.yaml
kubectl apply -f pgpool-secret.yaml
kubectl apply -f pgpool-svc.yaml
kubectl apply -f pgpool-deployment.yaml
kubectl apply -f psql-client.yaml
```

I haven't set up any sort of PostgreSQL migration infrastructure for this project, so you'll need to shell into the pgclient pod and create the `item` table. First, access the psql shell:

```bash
kubectl exec -it pg-client -- /bin/bash
kubectl get secret postgres-secrets -n database -o jsonpath="{.data.postgresql-password}" | base64 --decode
PGPASSWORD=<password> psql -h pgpool-svc -p 5432 -U postgres
```

Then, create the database and table:

```bash
CREATE DATABASE k8s;
\connect k8s
CREATE TABLE item (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);
```

Finally, get the URL of the API service:

```bash
minikube service api-svc --url
```

With this command, Minikube provides a tunnel from your local machine to the NodePort service.

Run a curl command to test the API!

```bash
curl -XPOST -H "Content-type: application/json" -d '{"name":"Noah","age":27}' 'http://127.0.0.1:58578/api/v1/items'
```