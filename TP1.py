## TSAMPI Augusta 

# Librairies utilisees
import os, requests
import json

# Je cree une fonction qui permet d'envoyer une requete HTTP GET a l'API et qui
# qui recupere les donees de la reponse. 
def get_weather(latitude, longitude):

    # url utilisee pour interroger l'API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json() # La donnee convertie est direcetemnt convertie en Json
    return data


# Utilisation du wrapper
# Ici je recupere les variables d'environnements saisies avec la librairie OS
latitude =  os.environ.get('LAT') 
longitude = os.environ.get('LONG') 
api_key = os.environ.get('API_KEY') 

# Test
# latitude =  31.00 
# longitude =  99.66  
# api_key = '84baed4a49b8309fc428e7a68dae972d'


#variable qui va recuperer le weather
weather_info = get_weather(latitude, longitude)

#Affichage du resultat
print(weather_info)

