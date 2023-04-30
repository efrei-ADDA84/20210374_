# Augusta TSAMPI 


import os
import requests
from fastapi import FastAPI
from datetime import datetime, timedelta


api_key=os.environ.get("API_KEY")

app = FastAPI()

@app.get("/")
async def read_item(latitude, longitude):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    result = requests.get(url)
    data = result.json()


    
    if response.status_code == 200:

       
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        daylight = sunset-sunrise

        city = data['name']
        country = data['sys']['country']
        
        meteo = data['weather'][0]['main']
        descri = data['weather'][0]['description']
        
        temperature = data['main']['temperature']
        feels = data['main']['feels_like']
        wind = data['wind']['speed']

        # Mise en forme de l'affichage en HTML
        html = """
            <h1> Augusta TSAMPI API TP2 - DEVOPS  </h1>
            <p><b> Latitude </b> : {} °</p>
            <p><b> Longitude </b> : {} °</p>
            <p><b> Ville </b> : {}</p>
            <p><b> Pays </b> : {}</p>
            <p><b> Température </b> : {} °C</p>
            <p><b> Température ressentie </b> : {} °C</p>
            <p><b> Temps </b> : {}</p>
            <p><b> Description du temps </b> : {}</p>
            <p><b> Force du vent </b> : {}</p>
            <p><b> Heure du lever du soleil </b> : {}</p>
            <p><b> Heure du coucher du soleil </b> : {}</p>
            <p><b> Durée de soleil </b> : {}</p>
        """.format(latitude, longitude, city, country, temperature, feels, meteo, descri, wind, sunrise, sunset, daylight)
            
    return data