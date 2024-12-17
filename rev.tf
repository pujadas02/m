provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"

  tags = {
    app = "myapp"
  }
}
resource "azurerm_network_security_group" "example" {
  name                = "example-nsg"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  tags = {
    a = "myApp" 
  }
}
# resource "azurerm_monitor_action_group" "example" {
#   name                = "example-action-group"
#   resource_group_name = "example-resource-group"
#   short_name          = "exampleag"
  
  
#   tags = {
#     app = "myApp" 
#   }
# }