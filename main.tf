provider "azurerm" {
  features {}
}
resource "azurerm_resource_group" "primary" {
  name     = "hi"
  location = "Eastuss"
}

resource "azurerm_resource_group" "rg_01" {
  name                = "mydomain.com"
  tags     = merge(local.tags.common_tags, local.tags.cvlt_backup.non_iaas)
  location = "k"
}
  

  
