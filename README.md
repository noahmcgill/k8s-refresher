# k8s refresher

This is a simple API written in Python (FastAPI) and deployed to a local Kubernetes cluster (Minikube).

## Development

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

## Production

### Run

```bash
fastapi run main.py
```
