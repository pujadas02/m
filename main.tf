provider "azurerm" {
  features {}
  skip_credentials_validation = true
}
resource "azurerm_resource_group" "primary" {
  name     = "hi"
  location = "Eastuss"
}

resource "azurerm_resource_group" "rg_01" {
  name                = "mydomain.com"
  tags     = merge(local.tags.cvlt_backup.non_iaas)
  location = "k"
}
  

  
