# Augusta TSAMPI 

import os
import requests
from fastapi import FastAPI


api_key=os.environ.get("API_KEY")

app = FastAPI()

@app.get("/")
async def read_item(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"
    result = requests.get(url)
    data = result.json()
            
    return data