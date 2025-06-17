locals {
  tags = {
    common_tags = {
      app                  = "Litmus IoT Edge"
      ppm_id_owner         = "Reeves, Lee"
      ppm_io_cc            = "81007982"
      environment          = "production"
      data_classification  = "confidential"
      app_owner_group      = "PNT-DATAINGESTION-GLOBAL"
      expert_centre        = "PNT-DATAINGESTION-GLOBAL"
      snapshotlifetime     = "1"
      cvlt_backup = "cvlt_no_backup"
    }

    cvlt_backup = {
      non_iaas = {
        business_criticality = "c"
      }

      app_server = {
        cvlt_backup        = "cvlt_vsa_file"
        ppm_billing_item   = "PET- MANUFACTURING DATA MANAGEMENT DESIGN AND PILOT"
        ppm_funding_source = "IO/CC"
      }
    }
  }
}
