provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "primary" {
  name     = "hi"
  location = "Eastuss"
}

resource "azurerm_monitor_diagnostic_setting" "logic20" {
  name                       = "OperationLogs"
  target_resource_id         = azurerm_logic_app_standard
  log_analytics_workspace_id = azurerm_log_analytics_workspace

  enabled_log {
    category = "WorkflowRuntime"
  }

  metric {
    category = "AllMetrics"
  }
}
