# dockerfile

FROM python:3.9.11

WORKDIR /app

RUN pip install flask

RUN pip install requests

COPY . .

EXPOSE 8081

CMD ["python", "Flash_App.py"]




