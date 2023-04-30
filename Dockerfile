# dockerfile

FROM python:3.9.11

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install requests

COPY requirements.txt .

COPY . .

EXPOSE 5000

CMD ["python", "Flash_app.py"]




