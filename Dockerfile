# dockerfile

FROM python:3.9.11

WORKDIR /app

RUN pip install flask==2.3.0

RUN pip install requests==2.29.0

RUN pip install --no-cache-dir  

ARG API_KEY 

COPY . .

EXPOSE 8081

CMD ["python", "Flash_App.py"]




