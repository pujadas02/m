provider "azurerm" {
  features {}
}
resource "azurerm_resource_group" "primary" {
  name     = "hi"
  location = "Eastuss"
  tags = local.tags.common_tags
}
resource "azurerm_monitor_diagnostic_setting" "logic20" {
  name                       = "OperationLogs"
  target_resource_id = "j"
  enabled_log {
    category = "WorkflowRuntime"
  }
  metric {
    category = "AllMetrics"
  }
}


resource "azurerm_dns_zone" "example-public" {
  name                = "mydomain.com"
  resource_group_name = "hi"
  tags = var.tags
}
resource "azurerm_resource_group" "rg_01" {
  name                = "mydomain.com"
  tags     = merge(local.tags.common_tags, local.tags.cvlt_backup.non_iaas)
  location = "k"
}
  

  
