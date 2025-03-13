FROM python:3.9.6-slim

WORKDIR /app

COPY src requirements.txt ./
RUN pip install -r ./requirements.txt

EXPOSE 8000

ENTRYPOINT [ "fastapi", "run", "./app.py" ]
