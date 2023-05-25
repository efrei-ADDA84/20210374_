# 20210374 - Augusta TSAMPI 
---------------------------------------------------------------

# DEVOPS - TP3 :

## Objectifs
- Mettre à disposition son code dans un repository Github
- Mettre à disposition son image (format API) sur Azure Container Registry (ACR) using
Github Actions
- Deployer sur Azure Container Instance (ACI) using Github Actions
---------------------------------------------------------------

## WORKFLOW
  
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


## Interet de l'utilisation d'une Github action pour deployer.
- On peut configurer des workflows personnalisés qui sont déclenchés automatiquement en fonction d'événements spécifiques tels que les pushs sur une branche ou les pull requests. Ce qui permet de réduire les erreurs humaines et d'accélérer le déploiement en évitant les étapes manuelles
- Avec GitHub Actions, on peut egalement visualiser et suivre l'état des workflows de déploiement directement dans le référentiel GitHub.
- une intégration facile avec d'autres outils, une visibilité et une évolutivité 



