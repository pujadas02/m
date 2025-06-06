provider "azurerm" {
  features {}
}
resource "azurerm_resource_group" "primary" {
  name     = "hi"
  location = "Eastuss"
  tags = var.tags
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
  tags = var.tags
}
