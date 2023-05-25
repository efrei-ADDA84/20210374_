# 20210374 - Augusta TSAMPI 
---------------------------------------------------------------

# DEVOPS - TP3 :

## Objectifs
- Mettre à disposition son code dans un repository Github
- Mettre à disposition son image (format API) sur Azure Container Registry (ACR) using
Github Actions
- Deployer sur Azure Container Instance (ACI) using Github Actions
---------------------------------------------------------------------

## ETAPES
- Création du fichier workflowtp3.yml dans le répertoire .github/workflows/ 
- Ensuite, on y insère les instructions suivantes:  
  - name: 20210374
  -  location: france south
  - environment-variables: API_KEY=${{ secrets.API_KEY }}
  - dns-name-label: devops-20210374


----------------------------------------------------------------------------------------------------

## WORKFLOW 

    ```  
    on: 
      push:
        branches: ["TP3"]
    name: Linux_Container_Workflow

    jobs:
        build-and-deploy:
            runs-on: ubuntu-latest
            steps:
            # checkout the repo
            - name: 'Checkout GitHub Action'
              uses: actions/checkout@main

            - name: 'Login via Azure CLI'
              uses: azure/login@v1
              with:
                creds: ${{ secrets.AZURE_CREDENTIALS }}

            - name: 'Build and push image'
              uses: azure/docker-login@v1
              with:
                login-server: ${{ secrets.REGISTRY_LOGIN_SERVER }}
                username: ${{ secrets.REGISTRY_USERNAME }}
                password: ${{ secrets.REGISTRY_PASSWORD }}
            - run: |
                docker build . -t ${{ secrets.REGISTRY_LOGIN_SERVER }}/20210374:${{ github.sha }}
                docker push ${{ secrets.REGISTRY_LOGIN_SERVER }}/20210374:${{ github.sha }}

            - name: 'Deploy to Azure Container Instances'
              uses: 'azure/aci-deploy@v1'
              with:
                resource-group: ${{ secrets.RESOURCE_GROUP }}
                dns-name-label: devops-20210374
                image: ${{ secrets.REGISTRY_LOGIN_SERVER }}/20210374:${{ github.sha }}
                registry-login-server: ${{ secrets.REGISTRY_LOGIN_SERVER }}
                registry-username: ${{ secrets.REGISTRY_USERNAME }}
                registry-password: ${{ secrets.REGISTRY_PASSWORD }}
                name: 20210374
                location: 'france south'
      ```
      

Voici une explication étape par étape :

- Déclencheur du workflow : Ce workflow est déclenché lorsqu'il y a un "push" sur la branche "TP3" du Github.

- Configuration du workflow : Le workflow est nommé "Linux_Container_Workflow".

- Étapes du workflow :

    - Étape 1 : "Checkout GitHub Action" - Cette étape récupère les fichiers du référentiel GitHub.
    -  Étape 2 : "Login via Azure CLI" - Cette étape utilise l'action azure/login@v1 pour se connecter à Azure en utilisant les informations d'identification stockées dans la variable secrets.AZURE_CREDENTIALS.
    - Étape 3 : "Build and push image" - Cette étape utilise l'action azure/docker-login@v1 pour se connecter au Azure Container Registry (ACR) en utilisant les informations d'identification du registre stockées dans les variables secrets.REGISTRY_LOGIN_SERVER, secrets.REGISTRY_USERNAME et secrets.REGISTRY_PASSWORD. Ensuite, elle construit l'image Docker en utilisant la commande docker build, lui attribue un tag basé sur le hachage du commit (${{ github.sha }}), puis pousse l'image vers le ACR.
    - Étape 4 : "Deploy to Azure Container Instances" - Cette étape utilise l'action azure/aci-deploy@v1 pour déployer l'image Docker sur Azure Container Instances (ACI). Elle spécifie le groupe de ressources (secrets.RESOURCE_GROUP), le nom DNS de l'instance (devops-20210374), l'image à déployer (${{ secrets.REGISTRY_LOGIN_SERVER }}/20210374:${{ github.sha }}), les informations d'identification du registre ACR, le nom de l'instance (20210374), et l'emplacement ('france south').

Ces étapes combinées permettent de construire et de déployer automatiquement une image Docker sur Azure Container Instances à chaque "push" sur la branche spécifiée.

-----------------------------------------------------------------------------------------------------------

## Application

```
import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')

def get_weather():

    lat = request.args.get('lat')
    lon = request.args.get('lon')
    key = "84baed4a49b8309fc428e7a68dae972d"
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)

  ```
  
  - Cet application Flask sert a obtenir les informations météorologiques en utilisant les coordonnées de latitude et de longitude fournies en tant que paramètres d'URL.
  -  L'API OpenWeatherMap est utilisée pour récupérer les données météorologiques correspondantes.


-------------------------------------------------------------------------
## Dockerfile

```
FROM python:3.9.11

WORKDIR /app

RUN pip install --no-cache-dir requests==2.29.0 flask==2.3.0


RUN pip install --no-cache-dir requests==2.29.0

ARG API_KEY 

COPY . .

CMD ["python", "App.py"]
```
-  ce Dockerfile crée une image Docker basée sur Python 3.9.11, installe les packages Python requests et flask, copie les fichiers du répertoire actuel dans l'image, puis définit le script App.py comme commande par défaut à exécuter lorsque le conteneur est démarré.


------------------------------------------------------------------

## Test

- Le workflow est déclenché lorsqu'il y a un "push" sur la branche "TP3" sur Github.

- Pour exécuter le projet, il suffit d'exécuter dans un terminal la commande: 
 >> curl "http://devops-20210374.francesouth.azurecontainer.io:8081/?lat=5.902785&lon=102.754175"
--------------------------------------------------------------------------------------------------------------

## Resultat du terminal

```
StatusCode        : 200
StatusDescription : OK
Content           : {
                      "base": "stations",
                      "clouds": {
                        "all": 96
                      },
                      "cod": 200,
                      "coord": {
                        "lat": 5.9028,
                        "lon": 102.7542
                      },
                      "dt": 1685050940,
                      "id": 1736405,
                      "main": {
                        "feels_like": 29.16...
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 715
                    Content-Type: application/json
                    Date: Thu, 25 May 2023 21:42:19 GMT
                    Server: Werkzeug/2.3.4 Python/3.9.11

                    {
                      "base": "stations",
                      "clouds"...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 715], [Content-Type, application/json], [Date, Thu, 25 May 2023 21:42:19 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 715

```

On peut aussi voir le resultat en format Json en suivant ce lien: 
>> http://devops-20210374.francesouth.azurecontainer.io:8081/?lat=5.902785&lon=102.754175

Resultat:
```
{
  "base": "stations",
  "clouds": {
    "all": 96
  },
  "cod": 200,
  "coord": {
    "lat": 5.9028,
    "lon": 102.7542
  },
  "dt": 1685050940,
  "id": 1736405,
  "main": {
    "feels_like": 29.16,
    "grnd_level": 983,
    "humidity": 76,
    "pressure": 1010,
    "sea_level": 1010,
    "temp": 26.89,
    "temp_max": 26.89,
    "temp_min": 26.89
  },
  "name": "Jertih",
  "sys": {
    "country": "MY",
    "sunrise": 1685055206,
    "sunset": 1685099928
  },
  "timezone": 28800,
  "visibility": 10000,
  "weather": [
    {
      "description": "overcast clouds",
      "icon": "04n",
      "id": 804,
      "main": "Clouds"
    }
  ],
  "wind": {
    "deg": 153,
    "gust": 3.05,
    "speed": 2.98
  }
}
```

---------------------------------------------------------------------------------------------------------------------------

## Interet de l'utilisation d'une Github action pour deployer.

- On peut configurer des workflows personnalisés qui sont déclenchés automatiquement en fonction d'événements spécifiques tels que les pushs sur une branche ou les pull requests. Ce qui permet de réduire les erreurs humaines et d'accélérer le déploiement en évitant les étapes manuelles
- Avec GitHub Actions, on peut egalement visualiser et suivre l'état des workflows de déploiement directement dans le référentiel GitHub.
- une intégration facile avec d'autres outils, une visibilité et une évolutivité 



