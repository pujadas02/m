from __future__ import annotations
from typing import Any
import requests
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureSnapshotLifetimeTagExistsCheck(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure environment tag exists. Valid Values are [production,legacy prod,disaster recovery,qa,QA,dev,Dev,test,Test,sandbox,Sandbox,N/A,NA]"
        id = "CCOE_AZ2_TAGS_2"
        supported_resources = ['azurerm_*']
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
        self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"

    def has_tags_support(self, resource_type):
        try:
            response = requests.get(f"{self.docs_url}{resource_type}.html.markdown", timeout=3)
            return response.status_code == 200 and "`tags`" in response.text
        except:
            return False

    def scan_resource_conf(self, conf):
        if not (address := conf.get("__address__", "")):
            return CheckResult.SKIPPED
            
        resource_type = address.split(".")[0][8:]
        
        if not self.has_tags_support(resource_type):
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
        return CheckResult.FAILED

check = EnsureSnapshotLifetimeTagExistsCheck()


