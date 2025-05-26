provider "azurerm" {
  features {}
  skip_credentials_validation = true
}
resource "azurerm_resource_group" "primary" {
  name     = "hi"
  location = "Eastuss"
}

resource "azurerm_resource_group" "rg_01" {
  name                = "mydomain.com"
  tags = {
  app                  = "Mars Integration Services"
  ppm_id_owner         = "Chen, Bruce"
  ppm_io_cc            = "11631976"
  environment          = "dev" # Allowed values are: 'production', 'legacy prod', 'disaster recovery', 'qa', 'QA', 'dev', 'Dev', 'test', 'Test', 'sandbox', 'Sandbox', 'N/A', 'NA'
  data_classification  = "Confidential"
  business_criticality = "A"
  app_owner_group      = "OPS-APPHOSTING-BAI-SOLACE"
  expert_centre        = "OPS-APPHOSTING-BAI-SOLACE"
  cvlt_backup          = "cvlt_no_backup"
  snapshotlifetime     = "0"
  datadog              = "monitored"
}
  location = "k"
}
  

  
