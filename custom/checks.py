from __future__ import annotations
import requests
from typing import Any
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureSnapshotLifetimeTagExistsCheck(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure data_classification tag exists. Valid Values are [highly confidential,Highly Confidential,confidential,Confidential,internal use only,internal,nonconfidential,Nonconfidential,non confidential,Non Confidential,N/A,NA]"
        id = "CCOE_AZ2_TAGS_4"
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
                data_classification = tags.get("data_classification")
                if data_classification is not None and data_classification in ["highly confidential", "Highly Confidential", "confidential", "Confidential", "internal use only", "internal", "nonconfidential", "Nonconfidential", "non confidential", "Non Confidential", "N/A", "NA"]:
                    return CheckResult.PASSED
                else:
                    return CheckResult.FAILED
        return CheckResult.FAILED

check = EnsureSnapshotLifetimeTagExistsCheck()

