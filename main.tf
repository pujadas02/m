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
  tags     = merge(var.tags.cvlt_backup.non_iaas, var.tags, local.tags.cvlt_backup.non_iaas, local.tags.common_tags)
  location = "k"
}
  

  
