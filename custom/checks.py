# from __future__ import annotations
# from typing import Any
# import requests
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class EnsureSnapshotLifetimeTagExistsCheck(BaseResourceCheck):
#     def __init__(self) -> None:
#         name = "Ensure environment tag exists. Valid Values are [production,legacy prod,disaster recovery,qa,QA,dev,Dev,test,Test,sandbox,Sandbox,N/A,NA]"
#         id = "CCOE_AZ2_TAGS_2"
#         supported_resources = ['azurerm_*']
#         categories = [CheckCategories.BACKUP_AND_RECOVERY]
#         super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
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
            
#         resource_type = address.split(".")[0][8:]
        
#         if not self.has_tags_support(resource_type):
#             return CheckResult.SKIPPED
                
#         tags = conf.get("tags")
#         if tags and isinstance(tags, list):
#             tags = tags[0]
#             if tags and isinstance(tags, dict):
                    
#                 environment = tags.get("environment")
#                 if environment is not None and environment in ["production", "legacy prod", "disaster recovery", "qa", "QA", "dev", "Dev", "test", "Test", "sandbox", "Sandbox", "N/A", "NA"]:
#                     return CheckResult.PASSED
#                 else:
#                     return CheckResult.FAILED
#         return CheckResult.FAILED

# check = EnsureSnapshotLifetimeTagExistsCheck()

from __future__ import annotations

from typing import Any
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureSnapshotLifetimeTagExistsCheck(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure environment tag exists. Valid Values are [production,legacy prod,disaster recovery,qa,QA,dev,Dev,test,Test,sandbox,Sandbox,N/A,NA]"
        id = "CCOE_AZ2_TAGS_2"
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
                    environment = tags.get("environment")
                    if environment is not None and environment in ["production", "legacy prod", "disaster recovery", "qa", "QA", "dev", "Dev", "test", "Test", "sandbox", "Sandbox", "N/A", "NA"]:
                        return CheckResult.PASSED 
                    else:
                        return CheckResult.FAILED
            else:
                if not tags:
                    return CheckResult.FAILED

check = EnsureSnapshotLifetimeTagExistsCheck()
