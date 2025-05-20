provider "azurerm" {
  features {}
}
resource "azurerm_resource_group" "primary" {
  name     = "hi"
  location = "Eastuss"
}


resource "azurerm_monitor_diagnostic_setting" "logic20" {
  name                       = "OperationLogs"
  enabled_log {
    category = "WorkflowRuntime"
  }
  metric {
    category = "AllMetrics"
  }
}


resource "azurerm_dns_zone" "example-public" {
  name                = "mydomain.com"
  tags = {
    app = "T1"
  }
}
resource "azurerm_resource_group" "rg_01" {
  name                = "mydomain.com"
  tags     = merge(local.tags.common_tags, local.tags.cvlt_backup.non_iaas)
}
  

  
