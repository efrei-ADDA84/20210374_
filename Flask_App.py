## TSAMPI Augusta 

# Librairies utilisees
import os, requests
import json
from flask import request, jsonify, Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET'])


def get_weather():

    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    API_KEY = os.environ.get('API_KEY')

    # url utilisee pour interroger l'API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    

    if response.status_code == 200:

       
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        daylight = sunset-sunrise

        latitude = data['coord']['lat']
        longitude = data['coord']['lon']

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
            
            
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=8081)
    # host='0.0.0.0' -> Pour accepter la connection avec n'importequel local host


