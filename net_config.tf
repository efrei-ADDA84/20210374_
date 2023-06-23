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