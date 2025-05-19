from __future__ import annotations
import requests
from typing import Any
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureSnapshotLifetimeTagExistsCheck(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure cvlt_backup tag exists. Valid Values are [cvlt_no_backup,cvlt_ida_ora,cvlt_ida_file,cvlt_ida_other,cvlt_ida_sql,cvlt_vsa_file,cvlt_vsa_sql,cvlt_vsa_ora]"
        id = "CCOE_AZ2_TAGS_3"
        supported_resources = ['azurerm_*']
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
            
        self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"
        self.excluded_resources = [
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
            "azurerm_role_assignment",
            "azurerm_resource_group",
            "azurerm_monitor_diagnostic_setting"
        ]
        def has_tags_support(self, resource_type):
        try:
            response = requests.get(f"{self.docs_url}{resource_type}.html.markdown", timeout=3)
            return response.status_code == 200 and "`tags`" in response.text
        except:
            return False
                
        def scan_resource_conf(self, conf):
        if not (address := conf.get("__address__", "")):
            return CheckResult.SKIPPED
        full_resource_type = address.split(".")[0]
        if any(excluded in full_resource_type for excluded in self.excluded_resources):
            return CheckResult.SKIPPED
        resource_type = full_resource_type[8:] 
        if not self.has_tags_support(resource_type):
            return CheckResult.SKIPPED    
                
        tags = conf.get("tags")
        if tags and isinstance(tags, list):
            tags = tags[0]
            if tags and isinstance(tags, dict):
                cvlt_backup = tags.get("cvlt_backup")
                if cvlt_backup is not None and cvlt_backup in ["cvlt_no_backup", "cvlt_ida_ora", "cvlt_ida_file", "cvlt_ida_other", "cvlt_ida_sql", "cvlt_vsa_file", "cvlt_vsa_sql", "cvlt_vsa_ora"]:
                    return CheckResult.PASSED
                else:
                    return CheckResult.FAILED
        return CheckResult.FAILED

check = EnsureSnapshotLifetimeTagExistsCheck()

