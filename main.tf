provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "primary" {
  name     = "hi"
  location = "Eastuss"
}

resource "azurerm_monitor_diagnostic_setting" "logic20" {
  name                       = "OperationLogs"
  target_resource_id         = azurerm_logic_app_standard.logic_apps["logic-marsis-np-eu2-20"].id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.log01.id

  enabled_log {
    category = "WorkflowRuntime"
  }

  metric {
    category = "AllMetrics"
  }
}
