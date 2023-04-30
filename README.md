# 20210374 - Augusta TSAMPI 
---------------------------------------------------------------

# DEVOPS - TP1 :

## Objectifs
- Créer un repository Github avec pour nom votre identifiant EFREI
- Créer un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude
(passées en variable d'environnement) en utilisant openweather API dans le langage de
programmation de votre choix (bash, python, go, nodejs, etc)
- Packager son code dans une image Docker
- Mettre à disposition son image sur DockerHub
- Mettre à disposition son code dans un repository Github


J'ai choisi de devellopper en python pour ce TP car c'est le language que j'utilise le plus.

## 1- Script Python 
Chaque ligne de code a un commentaire explicite dans le fichier TP1.py


j'ai tout d'abord cree un espace de travail et extrait mon API_Key depuis OpenWeather
> api_key = 84baed4a49b8309fc428e7a68dae972d

j'ai teste mon code python avec en entrees:
    > - latitude = 31.00 
    > - longitude = 99.66  
 sortie:
  >  {'coord': {'lon': 99.66, 'lat': 31}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'base': 'stations', 'main': {'temp': 1.63, 'feels_like': -2.15, 'temp_min': 1.63, 'temp_max': 1.63, 'pressure': 1008, 'humidity': 67, 'sea_level': 1008, 'grnd_level': 602}, 'visibility': 10000, 'wind': {'speed': 3.81, 'deg': 27, 'gust': 4.61}, 'snow': {'1h': 0.34}, 'clouds': {'all': 100}, 'dt': 1682673940, 'sys': {'country': 'CN', 'sunrise': 1682635223, 'sunset': 1682683034}, 'timezone': 28800, 'id': 1797039, 'name': 'Rulong', 'cod': 200}

## Docker file 

Definition de la version de python
> FROM python:3.9.11

Definition de l'espace de travail app
> WORKDIR /app

Installation des pip requis
> RUN pip install requests

Arguments 
ARG LAT
ARG LONG
ARG API_KEY

Copie des fichiers cree precedements et colle dans app
> COPY . .

> CMD ["python", "TP1.py"]

## Docker Hub :
on construit une nouvelle image docker en se basant sur le contenu DockerFile present dans le repertoire courant
> docker build . -t tp1_image:0.0.1

On renomme l'image
> docker tag tp1_image:0.0.1 atsugua10/tp1_repo

On publie l'image sur docker hub 
> docker push atsugua10/tp1_repo

On run le conteneur :
> docker run --env LAT="31.2504" --env LONG="-99.2506" --env API_KEY=84baed4a49b8309fc428e7a68dae972d atsugua10/tp1_repo

Sortie: 
> {'coord': {'lon': -99.2506, 'lat': 31.2504}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 26.1, 'feels_like': 26.1, 'temp_min': 25.97, 'temp_max': 26.47, 'pressure': 1007, 'humidity': 44}, 'visibility': 10000, 'wind': {'speed': 11.32, 'deg': 210, 'gust': 15.43}, 'clouds': {'all': 0}, 'dt': 1682695866, 'sys': {'type': 1, 'id': 3395, 'country': 'US', 'sunrise': 1682682908, 'sunset': 1682730817}, 'timezone': -18000, 'id': 4736286, 'name': 'Texas', 'cod': 200}

on recupere l'image depuis le repositorie
> docker pull atsugua10/tp1_repo

- Lien du repo GitHub : https://github.com/efrei-ADDA84/20210374_/blob/TP1

- Lien du repo DockerHub : https://hub.docker.com/repository/docker/atsugua10/tp1_repo/general



