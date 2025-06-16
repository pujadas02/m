# If you need to create local values, validate expressions and so on, use this place.
locals {

  tags = {
    app                  = "BigID"                   # App name according to CMDB
    ppm_id_owner         = "Castro, Dominic"         # Cost Center Owner 
    ppm_io_cc            = "11633521"                # Cost Center
    environment          = "production"                     # Must be one of these: "production","legacy prod","disaster recovery","qa","QA","dev","Dev","test","Test","sandbox","Sandbox","N/A","NA"
    data_classification  = "confidential"            # Must be one of these: "highly confidential","Highly Confidential","confidential","Confidential","internal use only","internal","nonconfidential","Nonconfidential","non confidential","Non Confidential","N/A","NA" 
    business_criticality = "c"                       # "A+","a+","A","a","B","b","C","c","Z","z","Tier 0","Tier0","T0,","tier 0","tier0","t0","Tier 1","Tier1","T1","tier 1","tier1","t1","N/A","NA"
    app_owner_group      = "BIGID_OPS_SUPPORT_GROUP" # Should be checked on CMDB on CI Application Owner Group
    expert_centre        = "BIGID_OPS_SUPPORT_GROUP" # This should be the same as the above
    snapshotlifetime     = "0"                       # Must be a string from 1 to 30
    cvlt_backup = "cvlt_no_backup"
  }
  vm_tags = {
    app                  = "BigID"                   # App name according to CMDB
    ppm_id_owner         = "william.dzmelyk@effem.com" # Cost Center Owner 
    ppm_io_cc            = "11633521"                # Cost Center
    environment          = "dev"                     # Must be one of these: "production","legacy prod","disaster recovery","qa","QA","dev","Dev","test","Test","sandbox","Sandbox","N/A","NA"
    data_classification  = "confidential"            # Must be one of these: "highly confidential","Highly Confidential","confidential","Confidential","internal use only","internal","nonconfidential","Nonconfidential","non confidential","Non Confidential","N/A","NA" 
    business_criticality = "c"                       # "A+","a+","A","a","B","b","C","c","Z","z","Tier 0","Tier0","T0,","tier 0","tier0","t0","Tier 1","Tier1","T1","tier 1","tier1","t1","N/A","NA"
    app_owner_group      = "BIGID_OPS_SUPPORT_GROUP" # Should be checked on CMDB on CI Application Owner Group
    expert_centre        = "BIGID_OPS_SUPPORT_GROUP" # This should be the same as the above
    snapshotlifetime     = "0"                       # Must be a string from 1 to 30
    ppm_billing_item     = "NA DATA PRIVACY RESOURCE POOL"
    ppm_funding_source   = "IO/CC"
  }
  cvlt_backup = {
    non_iaas = {
      cvlt_backup = "cvlt_no_backup"
    }
    sql_db = {
      cvlt_backup = "cvlt_ida_sql"
    }
  }

  role_definitions = {
    0 = "HDInsight on AKS Cluster Admin"
    1 = "Reader"
    2 = "Azure Kubernetes Service Contributor Role"
    3 = "Azure Kubernetes Service Cluster Admin Role"
    4 = "AcrPush"
    5 = "AcrPull"
    6 = "AcrImageSigner"
    7 = "Network Contributor"
  }

}
