output "ip_adresse" {
  value = azurerm_public_ip.tp4.ip_address
}

output "private_key" {
  value     = tls_private_key.ssh.private_key_pem
  sensitive = true
}