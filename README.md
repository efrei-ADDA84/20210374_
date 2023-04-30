# 20210374 - Augusta TSAMPI 
---------------------------------------------------------------

# DEVOPS - TP2 :

## Objectifs
- Configurer un workflow Github Action
- Transformer un wrapper en API
- Publier automatiquement a chaque push sur Docker Hub
- Mettre à disposition son image (format API) sur DockerHub
- Mettre à disposition son code dans un repository Github
---------------------------------------------------------------

## Transformation wrapper en API :

- Pour cela j'ai utilisé flask.

- J'ai ensuite créer un fichier configuration.py qui va se charger de récuperer les variables d'environnements comme la clef API ainsi que la latitude et la longitude.

-Puis le fichier j'ai cree Flash_App.py qui contient l'application flask. son code est quand a lui minutieusement commente

## Automatisation avec les actions GitHub :
  
name: TP2 Docker Image 

on:
  push:
    branches:
      - 'TP2'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
    
      - 
        uses: actions/checkout@v2
        name: Check out code
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      -
        name: Login to DockerHub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.TP_ID }}
          password: ${{ secrets.TP2_ACCES }}

      - 
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      -
        name: Build and push
        uses: docker/build-push-action@v3
        with:
          push: true
          tags: ${{ secrets.TP_ID }}/tp2_repo:0.0.3   
          context: . 

Dans GitHub on configure deux secrets : notre USERNAME qui correspond a TP_ID  et notre PASSWORD DockerHub qui corresponds a TP2_ACCES.

A chaque push sur la branche main, on build et on push l'image sur DockerHub.

Dans un premier teminal je lance la requete suivante:
> docker run --network host --env LAT="5.902785" --env LONG="102.754175"  --env API_KEY=84baed4a49b8309fc428e7a68dae972d atsugua10/tp1_repo
cette requete a ete lance avec la l'image du tp1 quie j'ai repull

Dans un deuxieme terminal je lance la requete suivante:
> curl "http://localhost:8081/?lat=5.902785&lon=102.754175"


## Sorties
> 



- Lien du repo GitHub : https://github.com/efrei-ADDA84/20210374_/edit/TP2/

- Lien du repo DockerHub : https://hub.docker.com/repository/docker/atsugua10/tp2_repo/general



