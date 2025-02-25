
# # Resource Group

resource "azurerm_storage_account" "storage_account01" {
  name                     = "mystorageacct01"
  resource_group_name       = azurerm_resource_group.rg01.name  # Reference to resource group name
  location                 = azurerm_resource_group.rg01.location  # Reference to location
  account_tier              = "Standard"
  account_replication_type = "LRS"
}
