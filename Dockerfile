# dockerfile

FROM python:3.9.11

WORKDIR /app

RUN pip install --no-cache-dir requests==2.29.0 flask==2.3.0


RUN pip install --no-cache-dir requests==2.29.0

ARG API_KEY 

COPY . .

CMD ["python", "App.py"]




