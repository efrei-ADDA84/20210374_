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
