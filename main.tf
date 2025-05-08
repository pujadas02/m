provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "primary" {
  name     = "hi"
  location = "Eastuss"
}


