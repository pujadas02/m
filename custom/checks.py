from __future__ import annotations

from typing import Any
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureResourcesLocation(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure resources are deployed only at allowed locations.(eastus2,centralus,westeurope,northeurope,southeastasia,eastasia,global,uksouth,chinanorth3)"
        id = "CCOE_AZ2_LOCATION_1"
        supported_resources = ['azurerm_*']
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: dict[str, list[Any]]) -> CheckResult:
        excluded_resource_types = [
            "azurerm_aadb2c_directory"
        ]
        resource_type = conf.get("__address__")
        if resource_type:
            for excluded_type in excluded_resource_types:
                if excluded_type in resource_type:
                    return CheckResult.SKIPPED
            location = conf.get("location")
            if location and isinstance(location, list):
                location = location[0]
                if location is not None and location in ["eastus2", "centralus", "westeurope", "northeurope", "southeastasia", "eastasia", "global", "uksouth", "EastUS2", "CentralUS", "NorthEurope", "WestEurope", "SoutheastAsia", "EastAsia", "chinanorth3", "ChinaNorth3"]:
                    return CheckResult.PASSED
                else:
                    return CheckResult.FAILED

check = EnsureResourcesLocation()












# from __future__ import annotations
# from typing import Any
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class EnsureSnapshotLifetimeTagExistsCheck(BaseResourceCheck):
#     def __init__(self) -> None:
#         name = "Ensure business_criticality tag exists. Valid Values are [A+,a+,A,a,B,b,C,c,Z,z,Tier 0,Tier0,T0,tier 0,tier0,t0,Tier 1,Tier1,T1,tier 1,tier1,t1,N/A,NA]"
#         id =  "CCOE_AZ2_16"
#         supported_resources = ['azurerm_*']
#         categories = [CheckCategories.BACKUP_AND_RECOVERY]
#         super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

#     def scan_resource_conf(self, conf: dict[str, list[Any]]) -> CheckResult:
#         print("Scanning resource:", conf)  # Debugging line to check if it's being executed
#         excluded_resource_types = [
#             "azurerm_virtual_machine_extension",
#             "azurerm_monitor_smart_detector_alert_rule",
#             "azurerm_monitor_action_group",
#             "azurerm_security_center_automation",
#             "azurerm_network_watcher",
#             "azurerm_network_connection_monitor",
#             "azurerm_network_watcher_flow_log",
#             "azurerm_virtual_hub",
#             "azurerm_management_group_template_deployment",
#             "azurerm_resource_group_template_deployment",
#             "azurerm_subscription_template_deployment",
#             "azurerm_tenant_template_deployment",
#             "azurerm_network_security_group",
#             "azurerm_network_security_rule",
#             "azurerm_automation_runbook",
#             "azurerm_api_connection",
#             "azurerm_role_assignment",
#             "azurerm_monitor_diagnostic_setting"
#             # "azurerm_resource_group"
#         ]
#         resource_type = conf.get("__address__")
#         if resource_type:
#             for excluded_type in excluded_resource_types:
#                 if excluded_type in resource_type:
#                     return CheckResult.SKIPPED
#             tags = conf.get("tags")
#             if tags and isinstance(tags, list):
#                 tags = tags[0]
#                 if tags and isinstance(tags, dict):
#                     business_criticality = tags.get("business_criticality")
#                     if business_criticality is not None and business_criticality in ["A+", "a+", "A", "a", "B", "b", "C", "c", "Z", "z", "Tier 0", "Tier0", "T0, ", "tier 0", "tier0", "t0", "Tier 1", "Tier1", "T1", "tier 1", "tier1", "t1", "N/A", "NA"]:
#                         return CheckResult.PASSED 
#                     else:
#                         return CheckResult.FAILED
#             else:
#                 if not tags:
#                     return CheckResult.FAILED

# check = EnsureSnapshotLifetimeTagExistsCheck()





# metadata:
#   name: "Ensure resource groups are deployed only at allowed locations.(eastus2,centralus,westeurope,northeurope,southeastasia,eastasia,global,uksouth,westeurope)"
#   id: "CCOE_AZ2_16"
#   category: "security"
#   severity: "HIGH"
#   description: "Ensure resources groups are deployed only at allowed locations."

# definition:
#   cond_type: "attribute"
#   resource_types:
#     - "azurerm_resource_group"
#   attribute: "location"
#   operator: "within"
#   value: ["eastus2", "centralus", "westeurope", "northeurope", "southeastasia", "eastasia", "uksouth"]


























# metadata:
#   name: "Deny the creation of private DNS"
#   id: "CKV_AZURE_001"
#   category: "Network"
#   severity: "HIGH"
# scope: 
#   provider: "azure"
#   # block_type: "resource"
# definition:
#   cond_type: "resource"
#   operator: "not_exists"
#   resource_types:
#     - "azurerm_private_dns_zone"





#this below one is 
# metadata:
#     name: "Allowed resource types"
#     id: "CKV_AZURE_001"
#     category: "General"
#     severity: "HIGH"

# scope:
#   provider: "azure"
# block_type: "resource"
# definition:
#     cond_type: "resource"
#     resource_types: 
#       - "azurerm_managed_disk"
#       - "azurerm_network_interface"
#       - "azurerm_virtual_network"
#       - "azurerm_virtual_machine_extension"
#       - "azurerm_snapshot"
#       - "azurerm_route_table"
#       - "azurerm_network_security_group"
#       - "azurerm_sql_virtual_machine"
#       - "azurerm_private_endpoint"
#       - "azurerm_lb"
#       - "azurerm_virtual_network"
#       - "azurerm_network_watcher"
#       - "azurerm_availability_set"
#       - "azurerm_sql_server"
#       - "azurerm_sql_database"
#       - "azurerm_storage_account"
#       - "azurerm_proximity_placement_group"
#       - "azurerm_cosmosdb_account"
#       - "azurerm_public_ip"
#       - "azurerm_log_analytics_workspace"
#       - "azurerm_key_vault"
#       - "azurerm_image"
#       - "azurerm_application_security_group"
#     operator: "exists"  


        
# metadata:
#   name: "ensures app tag exists"
#   id: "CKV_AZURE_001"
#   category: "tagging"
#   severity: "HIGH"

# scope: 
#       provider: "azure" 
#      block_type: "resource"
# definition:
#     or:
#       - cond_type: "attribute"
#         attribute: "tags.app"
#         operator: "not_exists"
#         resource_types:
#             - "azurerm_virtual_machine_extension"
#             - "azurerm_monitor_smart_detector_alert_rule"
#             - "azurerm_monitor_action_group"
#             - "azurerm_security_center_automation"
#             - "azurerm_network_watcher"
#             - "azurerm_network_connection_monitor"
#             - "azurerm_network_watcher_flow_log"
#             - "azurerm_virtual_hub"
#             - "azurerm_management_group_template_deployment"
#             - "azurerm_resource_group_template_deployment"
#             - "azurerm_subscription_template_deployment"
#             - "azurerm_tenant_template_deployment"
#             - "azurerm_network_security_group"
#             - "azurerm_network_security_rule"
#             - "azurerm_automation_runbook"
#             - "azurerm_api_connection"
#             - "azurerm_role_assignment"
#             # - "azurerm_resource_group"
#       - cond_type: "attribute"
#         attribute: "tags.app"
#         operator: "exists"
        
# # the above code checks all actions from wrokflow if they have app tag or not


# # metadata:
# #   name: "Ensures app tag exists"
# #   id: "CKV_AZURE_001"
# #   category: "tagging"
# #   severity: "HIGH"
# #   description: "Ensure that specific tag values are used."
# # scope:
# #   provider: "azure"        
# #   block_type: "resource"   
# # definition:
# #     cond_type: "attribute"  
# #     attribute: "tags.app"   
# #     operator: "exists"     

  
#     #     - "azure_virtual_machine"
#     #     - "Microsoft.Compute/virtualMachines/extensions"
#     #     - "Microsoft.AlertsManagement/smartDetectorAlertRules"
#     #     - "microsoft.insights/actiongroups"
#     #     - "Microsoft.Security/automations"
#     #     - "Microsoft.Network/networkWatchers"
#     #     - "Microsoft.Network/networkWatchers/connectionMonitors"
#     #     - "Microsoft.Network/networkWatchers/flowLogs"
#     #     - "Microsoft.Network/networkWatchers/lenses"
#     #     - "Microsoft.Network/networkWatchers/pingMeshes"
#     #     - "Microsoft.Network/virtualHubs"
#     #     - "Microsoft.Resources/deployments"
#     #     - "Microsoft.ResourceGraph/queries"
#     #     - "Microsoft.OperationsManagement/solutions"
#     #     - "Microsoft.Network/networkSecurityGroups"
#     #     - "Microsoft.Automation/AutomationAccounts/Runbooks"
#     #     - "microsoft.web/connections"
    

  
