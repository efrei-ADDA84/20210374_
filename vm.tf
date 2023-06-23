
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