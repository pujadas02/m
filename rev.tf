provider "azurerm" {
  features {}
  subscription_id = "your-allowed-subscription-id"
}

# Example to create a Private DNS Zone only in the allowed subscription
resource "azurerm_private_dns_zone" "dns_zone" {
  name                = "privatedns.example.com"
  resource_group_name = "example-rg"
}




# provider "azurerm" {
#   features {}
# }

# resource "azurerm_resource_group" "example" {
#   name     = "example-resources"
#   location = "East US"

#   tags = {
#     app = "myapp"
#   }
# }
# resource "azurerm_network_security_group" "example" {
#   name                = "example-nsg"
#   location            = azurerm_resource_group.example.location
#   resource_group_name = azurerm_resource_group.example.name

#   tags = {
#     a = "myApp" 
#   }
# }
# resource "azurerm_monitor_action_group" "example" {
#   name                = "example-action-group"
#   resource_group_name = "example-resource-group"
#   short_name          = "exampleag"
  
  
#   tags = {
#     app = "myApp" 
#   }
# }




# # provider "azurerm" {
# #   features {}
# # }

# # # Create Resource Group
# # resource "azurerm_resource_group" "vwan_rg" {
# #   name     = "vwan-deployment-rg"
# #   location = "East US"
# # }

# # # Create Virtual WAN
# # resource "azurerm_virtual_wan" "vwan" {
# #   name                = "example-vwan"
# #   location            = azurerm_resource_group.vwan_rg.location
# #   resource_group_name = azurerm_resource_group.vwan_rg.name
# # }

