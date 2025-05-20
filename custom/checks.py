from __future__ import annotations
from typing import Any
import requests
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureTagCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure business_criticality tag exists. Valid Values are [A+,a+,A,a,B,b,C,c,Z,z,Tier 0,Tier0,T0,,tier 0,tier0,t0,Tier 1,Tier1,T1,tier 1,tier1,t1,N/A,NA]"
        id = "CCOE_AZ2_TAGS_5"  
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
                business_criticality = tags.get("business_criticality")
                if business_criticality is not None and business_criticality in [
                    "A+", "a+", "A", "a", "B", "b", "C", "c", "Z", "z",
                    "Tier 0", "Tier0", "T0", "tier 0", "tier0", "t0",
                    "Tier 1", "Tier1", "T1", "tier 1", "tier1", "t1",
                    "N/A", "NA"
                ]:
                    return CheckResult.PASSED
                else:
                    return CheckResult.FAILED
        return CheckResult.FAILED

check = EnsureTagCheck()
