# dockerfile

FROM python:3.9.11

WORKDIR /app


RUN pip install requests

ARG LAT

ARG LONG

ARG API_KEY


COPY . .



CMD ["python", "TP1.py"]
