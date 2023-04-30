# Augusta TSAMPI 

import os
import requests
from fastapi import FastAPI


api_key=os.environ.get("API_KEY")

app = FastAPI()

@app.get("/")
async def read_item(latitude, longitude):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    result = requests.get(url)
    data = result.json()
            
    return data