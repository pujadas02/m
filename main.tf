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

resource "azurerm_resource_group" "secondary" {
  name     = "puja"
  location = "j"
  tags     = merge(local.tags, local.cvlt_backup.non_iaas)
}

resource "azurerm_dns_zone" "example-public" {
  name                = "mydomain.com"
  tags = {
    environment = "production"
  }
}
