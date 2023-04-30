# dockerfile

FROM python:3.9.11

WORKDIR /app

RUN pip install --no-cache-dir fastapi

RUN pip install --no-cache-dir uvicorn


RUN pip install --no-cache-dir requests==2.29.0

ARG API_KEY 

COPY . .

CMD ["uvicorn", "Flask_App:app", "--port", "8081", "--host", "0.0.0.0", "--reload"]




