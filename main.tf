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
resource "azurerm_dns_zone" "examplepublic" {
  name                = "mydomain.com"
  tags = {
    common_tags = {
      app                  = "Litmus IoT Edge"
      ppm_id_owner         = "Reeves, Lee"
      ppm_io_cc            = "81007982"
      environment          = "production"
      data_classification  = "confidential"
      business_criticality = "c"
      app_owner_group      = "PNT-DATAINGESTION-GLOBAL"
      expert_centre        = "PNT-DATAINGESTION-GLOBAL"
      snapshotlifetime     = "1"
    }

    cvlt_backup = {
      non_iaas = {
        cvlt_backup = "cvlt_no_backup"
      }

      app_server = {
        cvlt_backup        = "cvlt_vsa_file"
        ppm_billing_item   = "PET- MANUFACTURING DATA MANAGEMENT DESIGN AND PILOT"
        ppm_funding_source = "IO/CC"
      }
    }
  }
}
  
