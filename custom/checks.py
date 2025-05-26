# from __future__ import annotations
# from typing import Any
# import requests
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class EnsureTagCheck(BaseResourceCheck):
#     def __init__(self):
#         name = "Check for required tag"
#         id = "CUSTOM_TAG_CHECK"
#         supported_resources = ['azurerm_*']
#         super().__init__(name=name, id=id, categories=[CheckCategories.CONVENTION], supported_resources=supported_resources)
#         self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"
        
#     def has_tags_support(self, resource_type):
#         try:
#             response = requests.get(f"{self.docs_url}{resource_type}.html.markdown", timeout=3)
#             return response.status_code == 200 and "`tags`" in response.text
#         except:
#             return False

#     def scan_resource_conf(self, conf):
#         if not (address := conf.get("__address__", "")):
#             return CheckResult.SKIPPED   
#         resource_type = address.split(".")[0][8:]  # Remove 'azurerm_' prefix
#         if not self.has_tags_support(resource_type):
#             return CheckResult.SKIPPED    
#         tags = conf.get("tags", [{}])[0]
#         return CheckResult.PASSED if isinstance(tags, dict) and tags.get("business_criticality") else CheckResult.FAILED
# check = EnsureTagCheck()

# from __future__ import annotations
# from typing import Any
# import requests
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class EnsureTagCheck(BaseResourceCheck):
#     def __init__(self):
#         name = "Ensure business_criticality tag exists. Valid Values are [A+,a+,A,a,B,b,C,c,Z,z,Tier 0,Tier0,T0,,tier 0,tier0,t0,Tier 1,Tier1,T1,tier 1,tier1,t1,N/A,NA]"
#         id = "CCOE_AZ2_TAGS_5"  
#         supported_resources = ['azurerm_*']
#         categories = [CheckCategories.BACKUP_AND_RECOVERY]  
#         super().__init__(name=name, id=id, 
#                         categories=categories,
#                         supported_resources=supported_resources)
#         self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"
        
#         self.excluded_resources = [
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
#         ]

#     def has_tags_support(self, resource_type):
#         try:
#             response = requests.get(f"{self.docs_url}{resource_type}.html.markdown", timeout=3)
#             return response.status_code == 200 and "`tags`" in response.text
#         except:
#             return False

#     def scan_resource_conf(self, conf):
#         if not (address := conf.get("__address__", "")):
#             return CheckResult.SKIPPED
            
#         full_resource_type = address.split(".")[0]
        
#         if any(excluded in full_resource_type for excluded in self.excluded_resources):
#             return CheckResult.SKIPPED
            
#         resource_type = full_resource_type[8:]  # Remove 'azurerm_' prefix
        
#         if not self.has_tags_support(resource_type):
#             return CheckResult.SKIPPED
                
#         tags = conf.get("tags")
#         if tags and isinstance(tags, list):
#             tags = tags[0]
#             if tags and isinstance(tags, dict):
#                 business_criticality = tags.get("business_criticality")
#                 if business_criticality is not None and business_criticality in [
#                     "A+", "a+", "A", "a", "B", "b", "C", "c", "Z", "z",
#                     "Tier 0", "Tier0", "T0", "tier 0", "tier0", "t0",
#                     "Tier 1", "Tier1", "T1", "tier 1", "tier1", "t1",
#                     "N/A", "NA"
#                 ]:
#                     return CheckResult.PASSED
#                 else:
#                     return CheckResult.FAILED
#         return CheckResult.FAILED

# check = EnsureTagCheck()


from __future__ import annotations

from typing import Any
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureSnapshotLifetimeTagExistsCheck(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure app,app_owner_group,ppm_io_cc,ppm_id_owner,expert_centre tag exists."
        id = "CCOE_AZ2_TAGS_6"
        supported_resources = ['azurerm_*']
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: dict[str, list[Any]]) -> CheckResult:
        excluded_resource_types = [
            "azurerm_virtual_machine_extension",
            "azurerm_monitor_smart_detector_alert_rule",
            "azurerm_monitor_action_group",
            "azurerm_security_center_automation",
            "azurerm_network_watcher",
            "azurerm_network_connection_monitor",
            "azurerm_network_watcher_flow_log",
            "azurerm_virtual_hub",
            "azurerm_management_group_template_deployment",
            "azurerm_resource_group_template_deployment",
            "azurerm_subscription_template_deployment",
            "azurerm_tenant_template_deployment",
            "azurerm_network_security_group",
            "azurerm_network_security_rule",
            "azurerm_automation_runbook",
            "azurerm_api_connection",
            "azurerm_role_assignment"
        ]
        resource_type = conf.get("__address__")
        if resource_type:
            for excluded_type in excluded_resource_types:
                if excluded_type in resource_type:
                    return CheckResult.SKIPPED
            tags = conf.get("tags")
            if tags and isinstance(tags, list):
                tags = tags[0]
                if tags and isinstance(tags, dict):
                    app = tags.get("app")
                    app_owner_group = tags.get("app_owner_group")
                    ppm_io_cc = tags.get("ppm_io_cc")
                    ppm_id_owner = tags.get("ppm_id_owner")
                    expert_centre = tags.get("expert_centre")
                    if app is not None and app_owner_group is not None and ppm_io_cc is not None and ppm_id_owner is not None and expert_centre is not None:
                        return CheckResult.PASSED 
                    else:
                        return CheckResult.FAILED
            else:
                if not tags:
                    return CheckResult.FAILED

check = EnsureSnapshotLifetimeTagExistsCheck()
