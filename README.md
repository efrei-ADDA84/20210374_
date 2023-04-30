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

- J'ai utiliser le module Python fastAPI pour transformer mon wrapper en API. 

- J'ai d'abord cree l'application Flask_App.py qui contient l'application FastApi. son code est quand a lui minutieusement commente

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
> docker pull atsugua10/tp2_repo:0.0.3
> docker run -p 8081:8081 --env API_KEY=84baed4a49b8309fc428e7a68dae972d atsugua10/tp2_repo:0.0.3
cette requete a ete lance avec la l'image du tp1 quie j'ai repull

Dans un deuxieme terminal je lance la requete suivante:
> curl "http://localhost:8081/?lat=5.902785&lon=102.754175"


## Sorties
Aller a l'adresse 
> http://192.168.0.24:8081
ou
> http://192.168.0.24:8081

##Partie optionelle
Lint Errors
> - name: Ckecking des Lint errors avec Hadolint
      uses: hadolint/hadolint-action@v3.1.0
      with:
        dockerfile: Dockerfile



- Lien du repo GitHub : https://github.com/efrei-ADDA84/20210374_/edit/TP2/

- Lien du repo DockerHub : https://hub.docker.com/repository/docker/atsugua10/tp2_repo/general



