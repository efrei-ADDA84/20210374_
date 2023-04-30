# dockerfile

FROM python:3.9.11

WORKDIR /app

RUN pip install flask

RUN pip install requests

ARG LAT

ARG LONG

ARG API_KEY

COPY . .

EXPOSE 5000

CMD ["python", "Flash_App.py"]




