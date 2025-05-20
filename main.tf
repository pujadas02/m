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
    app = "T1",
    app_owner_group = "tf",
    ppm_io_cc = "j",
    ppm_id_owner = "kk",
    expert_centre = "hi"
  }
}
