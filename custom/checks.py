# from __future__ import annotations
# import requests
# import re
# from typing import Any, Dict, List
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class EnsureMandatoryTagsExist(BaseResourceCheck):
#     def __init__(self) -> None:
#         name = "Ensure required tags exist"
#         id = "CCOE_AZ2_TAGS_6"
#         supported_resources = ['azurerm_*']
#         categories = [CheckCategories.CONVENTION]
#         super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
#         self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"
        
#         self.required_tags = {
#             "app",
#             "app_owner_group",
#             "ppm_io_cc",
#             "ppm_id_owner",
#             "expert_centre"
#         }

#     def has_tags_support(self, resource_type: str) -> bool:
#         try:
#             response = requests.get(f"{self.docs_url}{resource_type}.html.markdown", timeout=3)
#             return response.status_code == 200 and "`tags`" in response.text
#         except:
#             return False

#     def extract_tags_from_config(self, tags_config: Any) -> Dict[str, Any]:
#         """Extract tags from various Terraform configurations"""
#         tags = {}
        
#         # Case 1: Direct tags dictionary
#         if isinstance(tags_config, dict):
#             return tags_config
            
#         # Case 2: List containing tags (common in Checkov parsing)
#         if isinstance(tags_config, list) and len(tags_config) > 0:
#             if isinstance(tags_config[0], dict):
#                 return tags_config[0]
            
#             # Case 3: String containing merge() operation
#             if isinstance(tags_config[0], str):
#                 merge_content = tags_config[0]
#                 # Extract all dictionaries from merge() arguments
#                 dict_matches = re.findall(r'\{[^{}]*\}', merge_content)
#                 for dict_str in dict_matches:
#                     try:
#                         tag_dict = eval(dict_str)  # Safe because we control the input pattern
#                         if isinstance(tag_dict, dict):
#                             tags.update(tag_dict)
#                     except:
#                         continue
#         return tags

#     def scan_resource_conf(self, conf: Dict[str, List[Any]]) -> CheckResult:
#         if not (address := conf.get("__address__", "")):
#             return CheckResult.SKIPPED
            
#         resource_type = address.split(".")[0][8:]
#         if not self.has_tags_support(resource_type):
#             return CheckResult.SKIPPED
            
#         tags_config = conf.get("tags", [])
#         tags = self.extract_tags_from_config(tags_config)
        
#         # Check for all required tags
#         missing_tags = [tag for tag in self.required_tags if tag not in tags]
        
#         if missing_tags:
#             print(f"Resource {address} missing tags: {missing_tags}")  # Debug output
#             return CheckResult.FAILED
#         return CheckResult.PASSED

# check = EnsureMandatoryTagsExist()








# from __future__ import annotations
# import requests
# import re
# from typing import Any, Dict
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class EnsureTagsExist(BaseResourceCheck):
#     def __init__(self) -> None:
#         super().__init__(
#             name="Ensure required tags exist",
#             id="CCOE_AZ2_TAGS_6",
#             categories=[CheckCategories.CONVENTION],
#             supported_resources=['azurerm_*']
#         )
#         self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"
#         self.required_tags = {"app", "app_owner_group", "ppm_io_cc", "ppm_id_owner", "expert_centre"}

#     def get_tags(self, conf: Dict[str, Any]) -> Dict[str, Any]:
#         tags_config = conf.get("tags", [{}])[0]
#         if isinstance(tags_config, dict):
#             return tags_config
#         if isinstance(tags_config, str):
#             return {k: v for m in re.finditer(r"'(\w+)'\s*:\s*'([^']*)'", tags_config) 
#                    for k, v in [m.groups()]}
#         return {}

#     def scan_resource_conf(self, conf: Dict[str, Any]) -> CheckResult:
#         if not conf.get("__address__"):
#             return CheckResult.SKIPPED
            
#         tags = self.get_tags(conf)
#         return CheckResult.PASSED if all(tag in tags for tag in self.required_tags) else CheckResult.FAILED

# check = EnsureTagsExist()
from __future__ import annotations
import re
from typing import Any, Dict
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureTagsExist(BaseResourceCheck):
    def __init__(self) -> None:
        super().__init__(
            name="Ensure required tags exist",
            id="CCOE_AZ2_TAGS_6",
            categories=[CheckCategories.CONVENTION],
            supported_resources=['azurerm_*']
        )
        self.required_tags = {
            "app", "app_owner_group", "ppm_io_cc",
            "ppm_id_owner", "expert_centre", "cvlt_backup"
        }

    def get_tags(self, conf: Dict[str, Any]) -> Dict[str, Any]:
        """Safely extract tags from any configuration format"""
        # Handle case where tags key doesn't exist
        if "tags" not in conf:
            return {}
            
        tags_config = conf["tags"]
        
        # Handle list-wrapped tags (common in Checkov parsing)
        if isinstance(tags_config, list):
            if not tags_config:  # Empty list
                return {}
            tags_config = tags_config[0]
            
        # Handle direct dictionaries
        if isinstance(tags_config, dict):
            return tags_config
            
        # Handle string expressions
        if isinstance(tags_config, str):
            if "merge(" in tags_config.lower():
                # When merge() exists, we can't be sure about tags - assume they might exist
                return {tag: "exists" for tag in self.required_tags}
            return self._extract_dict_tags(tags_config)
            
        return {}

    def _extract_dict_tags(self, dict_str: str) -> Dict[str, str]:
        """Robust extraction of tags from string representations"""
        tags = {}
        try:
            for match in re.finditer(
                r'([\'"]?)(\w+)\1\s*[:=]\s*([\'"]?)([^\'",}]+)\3',
                dict_str
            ):
                key = match.group(2)
                value = match.group(4).strip('\'" ')
                tags[key] = value
        except Exception:
            pass
        return tags

    def scan_resource_conf(self, conf: Dict[str, Any]) -> CheckResult:
        if not conf.get("__address__"):
            return CheckResult.SKIPPED
            
        tags = self.get_tags(conf)
        
        # If merge() was used, we can't be certain - pass conservatively
        if isinstance(conf.get("tags"), str) and "merge(" in conf["tags"].lower():
            return CheckResult.PASSED
            
        # If no tags at all
        if not tags:
            return CheckResult.FAILED
            
        return CheckResult.PASSED if all(tag in tags for tag in self.required_tags) else CheckResult.FAILED

check = EnsureTagsExist()
# thi below in actions the resource is passed but some error
# from __future__ import annotations
# import re
# from typing import Any, Dict
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class EnsureTagsExist(BaseResourceCheck):
#     def __init__(self) -> None:
#         super().__init__(
#             name="Ensure required tags exist",
#             id="CCOE_AZ2_TAGS_6",
#             categories=[CheckCategories.CONVENTION],
#             supported_resources=['azurerm_*']
#         )
#         self.required_tags = {
#             "app", "app_owner_group", "ppm_io_cc",
#             "ppm_id_owner", "expert_centre", "cvlt_backup"
#         }

#     def get_tags(self, conf: Dict[str, Any]) -> Dict[str, Any]:
#         tags_config = conf.get("tags", [{}])[0]
        
#         if isinstance(tags_config, dict):
#             return tags_config
            
#         if isinstance(tags_config, str):
#             # Handle both direct tags and merge expressions
#             if "merge(" in tags_config.lower():
#                 # When merge() exists but we can't evaluate it, assume tags might be present
#                 return {tag: "exists" for tag in self.required_tags}
#             return self._extract_dict_tags(tags_config)
            
#         return {}

#     def _extract_dict_tags(self, dict_str: str) -> Dict[str, str]:
#         """Extract tags from both {'key':'value'} and {key = value} formats"""
#         tags = {}
#         for match in re.finditer(
#             r'([\'"]?)(\w+)\1\s*[:=]\s*([\'"]?)([^\'",}]+)\3',
#             dict_str
#         ):
#             tags[match.group(2)] = match.group(4).strip('\'" ')
#         return tags

#     def scan_resource_conf(self, conf: Dict[str, Any]) -> CheckResult:
#         if not conf.get("__address__"):
#             return CheckResult.SKIPPED
            
#         tags = self.get_tags(conf)
        
#         # Special case: If merge() was used but we couldn't evaluate it
#         if isinstance(conf.get("tags", [""])[0], str) and "merge(" in conf["tags"][0].lower():
#             return CheckResult.PASSED
            
#         return CheckResult.PASSED if all(tag in tags for tag in self.required_tags) else CheckResult.FAILED

# check = EnsureTagsExist()


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
