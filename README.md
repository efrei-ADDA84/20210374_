# 20210374_ - Augusta TSAMPI

## TP4 - DEVOPS : Cloud Terraform

## Objectifs

- Créer une machine virtuelle Azure (VM) avec une adresse IP publique dans un réseau
existant ( network-tp4 )
- Utiliser Terraform
- Se connecter à la VM avec SSH
- Comprendre les différents services Azure (ACI vs. AVM)
- Mettre à disposition son code dans un repository Github

## choix techniques

### Contenu du repo

Cette branche contient:
- un fichier provider.tf qui va permettre à Terraform d'utiliser le fournisseur AzureRM et d'établir la connexion avec l'abonnement Azure spécifié
- un fichier net_config ou les ressources vont permettent de déployer une adresse IP publique, une interface réseau, de générer une paire de clés SSH et de créer un fichier local contenant la clé publique SSH générée.
- un fichier vm.tf ou se trouvent les configurations qui permettent de créer la machine virtuelle Linux dans Azure
- un ficher data.tf  qui sera utilisé  dans le processus de déploiement pour référencer les ID des ressources créées.
- un fichier variable.tf qui définit les variables utilisées dans la configuration Terraform pour personnaliser le déploiement des ressources Azure.
- 

## Fichiers 
- data.tf
```
    data "azurerm_subnet" "tp4" {
      name                 = var.subnet-name
      virtual_network_name = var.network-name
      resource_group_name  = var.ressource-group
    }
    
    output "subnet_id" {
      value = data.azurerm_subnet.tp4.id
    }
    
    data "azurerm_virtual_network" "tp4" {
      name                = var.network-name
      resource_group_name = var.ressource-group
    }
    
    output "virtual_network_id" {
      value = data.azurerm_virtual_network.tp4.id
    }
```
  
- Une définition de données pour la ressource de sous-réseau Azure tp4, avec le nom du sous-réseau, le nom du réseau virtuel et le nom du groupe de ressources spécifiés en tant que variables.
- Une sortie nommée "subnet_id" qui renvoie l'ID du sous-réseau Azure défini dans la ressource de sous-réseau.
- Une définition de données pour un réseau virtuel Azure, avec le nom du réseau virtuel et le nom du groupe de ressources spécifiés en tant que variables.
-Une sortie nommée "virtual_network_id" qui renvoie l'ID du réseau virtuel Azure défini dans la ressource de réseau virtuel.

- le fichier vm.tf
```
    resource "azurerm_linux_virtual_machine" "tp4" {
      name                = "devops-20210374"
      resource_group_name = var.ressource-group
      location            = var.region
      size                = "Standard_D2s_v3"
      admin_username      = var.username
      network_interface_ids = [
        azurerm_network_interface.tp4.id
      ]
    
      admin_ssh_key {
        username   = var.username
        public_key = tls_private_key.ssh.public_key_openssh
      }
    
      os_disk {
        caching              = "ReadWrite"
        storage_account_type = "Standard_LRS"
      }
    
      source_image_reference {
        publisher = "Canonical"
        offer     = "UbuntuServer"
        sku       = "16.04-LTS"
        version   = "latest"
      }
    }
```

ce fichier contient
- Les propriétés de la ressource comprennent qui sont: le nom du groupe de ressources, l'emplacement, la taille de la machine virtuelle, le nom d'utilisateur de l'administrateur spécifié en tant que variable, et une liste d'identifiants d'interface réseau pour connecter la machine virtuelle au réseau.
- Une clé SSH configurée avec le nom d'utilisateur spécifié en tant que variable et la clé publique SSH provenant de tls_private_key.ssh.public_key_openssh.
- Une référence d'image source

- provider.tf
    
```
  terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

provider "azurerm" {
  features {}
  
  subscription_id = "765266c6-9a23-4638-af32-dd1e32613047"
}
```

  - variable.tf

```
    variable "region" {
  type    = string
  default = "francecentral"
}

variable "ressource-group" {
  type    = string
  default = "ADDA84-CTP"
}

variable "network-name" {
  type    = string
  default = "network-tp4"
}

variable "subnet-name" {
  type    = string
  default = "internal"
}

variable "username" {
  type    = string
  default = "devops"
}

variable "subscription_id" {
  type    = string
  default = "765266c6-9a23-4638-af32-dd1e32613047"
}
```

    les variables sont respectivement:
      - la région dans laquelle les ressources doivent être déployées. Elle est de type string et a une valeur par défaut de "francecentral"
      -  le nom du groupe de ressources dans lequel les ressources doivent être créées. Elle est de type string et a une valeur par défaut de "ADDA84-CTP".
      -  le nom du réseau virtuel dans lequel les ressources doivent être connectées. Elle est de type string et a une valeur par défaut de "network-tp4".
      -  le nom du sous-réseau dans lequel les ressources doivent être placées. Elle est de type string et a une valeur par défaut de "internal".
      -  le nom d'utilisateur de l'administrateur pour les machines virtuelles déployées. Elle est de type string et a une valeur par défaut de "devops".
      -  et enfin l'ID d'abonnement Azure dans lequel les ressources doivent être créées. Elle est de type string et a une valeur par défaut de "765266c6-9a23-4638-af32-dd1e32613047".

- net_config
```
  resource "azurerm_public_ip" "tp4" {
  name                = "public_ip"
  resource_group_name = var.ressource-group
  location            = var.region
  allocation_method   = "Static"

  tags = {
    environment = "Production"
  }
}

resource "azurerm_network_interface" "tp4" {
  name                = "network_interface_name"
  location            = var.region
  resource_group_name = var.ressource-group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = data.azurerm_subnet.tp4.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.tp4.id
  }
}

resource "tls_private_key" "ssh" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "local_file" "public_key" {
  content  = tls_private_key.ssh.public_key_openssh
  filename = "ssh_public_key.pub"
}
```

ce fichier contient respectivement:
- azurerm_public_ip : utilisée pour créer une adresse IP publique. Elle définie avec le nom "public_ip" et est associée au groupe de ressources spécifié dans la variable var.ressource-group
- azurerm_network_interface : utilisée pour créer une interface réseau. Elle est définie avec le nom "network_interface_name" et est associée au groupe de ressources spécifié dans la variable var.ressource-group. Elle est egalement liée au sous-réseau spécifié par data.azurerm_subnet.tp4.id
- tls_private_key :  utilisée pour générer une paire de clés privée/publique SSH. Elle est configurée avec un algorithme RSA et une taille de 4096 bits
- local_file : utilisée pour créer un fichier local contenant la clé publique SSH générée précédemment. Le contenu de la clé publique est défini comme tls_private_key.ssh.public_key_openssh et le nom de fichier est défini comme "ssh_public_key.pub".



## intérêt de l'utilisation de
Terraform pour deployer des ressources sur le cloud plutôt que la CLI ou l'interface
utilisateur
- Terraform offre une approche déclarative et basée sur le code pour le déploiement et la gestion de l'infrastructure cloud
- Terraform offre une approche déclarative et basée sur le code pour le déploiement et la gestion de l'infrastructure cloud
    
