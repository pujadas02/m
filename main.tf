provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "primary" {
  name     = join("-", ["rg", var.app_name, var.env, var.location_abr, "01"])
  location = "Eastuss"
}


