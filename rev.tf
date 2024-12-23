provider "azurerm" {
  features {}
}

# # Resource Group
# resource "azurerm_resource_group" "example" {
#   name     = "example-resources"
#   location = "East US"
# }

# Managed Disk
resource "azurerm_managed_disk" "example_disk" {
  name                 = "example-managed-disk"
  resource_group_name  = azurerm_resource_group.example.name
  location             = azurerm_resource_group.example.location
  
  storage_account_type = "Standard_LRS"
  create_option        = "Empty"
}

# Virtual Network
resource "azurerm_virtual_network" "example_vnet" {
  name                = "example-vnet"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  address_space       = ["10.0.0.0/16"]
}

# Network Interface
resource "azurerm_network_interface" "example_nic" {
  name                = "example-nic"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  ip_configuration {
    name                          = "example-ipconfig"
    subnet_id                     = azurerm_virtual_network.example_vnet.subnet[0].id
    private_ip_address_allocation = "Dynamic"
  }
}

# Storage Account
resource "azurerm_storage_account" "example_storage" {
  name                     = "examplestorageacct"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier              = "Standard"
  account_replication_type = "LRS"
}

# SQL Server
resource "azurerm_sql_server" "example_sql_server" {
  name                         = "example-sql-server"
  resource_group_name          = azurerm_resource_group.example.name
  location                     = azurerm_resource_group.example.location
  version                      = "12.0"
  administrator_login          = "sqladmin"
  administrator_login_password = "password1234!"

  tags = {
    environment = "production"
  }
}





# provider "azurerm" {
#   features {}
#   subscription_id = "your-allowed-subscription-id"
# }

# # Example to create a Private DNS Zone only in the allowed subscription
# resource "azurerm_private_dns_zone" "dns_zone" {
#   name                = "privatedns.example.com"
#   resource_group_name = "example-rg"
# }






















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

