provider "azurerm" {
  features {}
}

resource "azurerm_monitor_diagnostic_setting" "logic" {
  for_each                   = local.logicapploop
  name                       = "OperationLogs"
  target_resource_id         = azurerm_logic_app_standard.logic[each.key].id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.log01.id
  enabled_log {
    category = "WorkflowRuntime"
  }
  metric {
    category = "AllMetrics"
  }
}

