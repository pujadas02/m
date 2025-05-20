from __future__ import annotations
import requests
from typing import Any, Dict, List
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureMandatoryTagsExist(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure required tags exist"
        id = "CCOE_AZ2_TAGS_6"
        supported_resources = ['azurerm_*']
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
        self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"
        
        # List of required tags
        self.required_tags = {
            "app",
            "app_owner_group",
            "ppm_io_cc",
            "ppm_id_owner",
            "expert_centre"
        }

    def has_tags_support(self, resource_type: str) -> bool:
        try:
            response = requests.get(f"{self.docs_url}{resource_type}.html.markdown", timeout=3)
            return response.status_code == 200 and "`tags`" in response.text
        except:
            return False

    def get_tag_value(self, tags: Dict[str, Any], tag_name: str) -> Any:
        """Recursively check for tag in merged structures"""
        if tag_name in tags:
            return tags[tag_name]
        for value in tags.values():
            if isinstance(value, dict):
                found = self.get_tag_value(value, tag_name)
                if found is not None:
                    return found
        return None

    def scan_resource_conf(self, conf: Dict[str, List[Any]]) -> CheckResult:
        # Skip if no address
        if not (address := conf.get("__address__", "")):
            return CheckResult.SKIPPED
            
        # Check tag support
        resource_type = address.split(".")[0][8:]
        if not self.has_tags_support(resource_type):
            return CheckResult.SKIPPED
            
        # Get tags configuration
        tags_config = conf.get("tags")
        if not tags_config or not isinstance(tags_config, list):
            return CheckResult.FAILED
            
        tags = tags_config[0]
        if not isinstance(tags, dict):
            return CheckResult.FAILED
            
        # Check for all required tags
        missing_tags = []
        for tag in self.required_tags:
            if not self.get_tag_value(tags, tag):
                missing_tags.append(tag)
                
        return CheckResult.PASSED if not missing_tags else CheckResult.FAILED

check = EnsureMandatoryTagsExist()

# from __future__ import annotations
# import requests
# from typing import Any
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class EnsureSnapshotLifetimeTagExistsCheck(BaseResourceCheck):
#     def __init__(self) -> None:
#         name = "Ensure app,app_owner_group,ppm_io_cc,ppm_id_owner,expert_centre tag exists."
#         id = "CCOE_AZ2_TAGS_6"
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
#                 app = tags.get("app")
#                 app_owner_group = tags.get("app_owner_group")
#                 ppm_io_cc = tags.get("ppm_io_cc")
#                 ppm_id_owner = tags.get("ppm_id_owner")
#                 expert_centre = tags.get("expert_centre")
#                 if app is not None and app_owner_group is not None and ppm_io_cc is not None and ppm_id_owner is not None and expert_centre is not None:
#                     return CheckResult.PASSED
#                 else:
#                     return CheckResult.FAILED
#         return CheckResult.FAILED

# check = EnsureSnapshotLifetimeTagExistsCheck()
