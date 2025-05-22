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


import os
import hcl2
from typing import Dict, Any, List
from checkov.common.models.enums import CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class EnsureTagsExist(BaseResourceCheck):
    def __init__(self):
        super().__init__(
            name="Ensure required tags exist",
            id="CCOE_AZ2_TAGS_6",
            supported_resources=["azurerm_*"],
            categories=["Convention"],
        )
        self.required_tags = {
            "app", "app_owner_group", "ppm_io_cc",
            "ppm_id_owner", "expert_centre", "cvlt_backup"
        }
        self.locals_cache = {}  # Stores parsed locals from all .tf files

    def scan_resource_conf(self, conf: Dict[str, Any]) -> CheckResult:
        if not conf.get("__address__"):
            return CheckResult.SKIPPED

        # Parse all .tf files to extract locals (once)
        if not self.locals_cache:
            self._parse_all_tf_files(os.path.dirname(conf["__file__"]))

        tags = self._resolve_tags(conf.get("tags", [{}])[0])
        return CheckResult.PASSED if all(tag in tags for tag in self.required_tags) else CheckResult.FAILED

    def _parse_all_tf_files(self, dir_path: str):
        """Extract all locals from Terraform files in a directory"""
        for filename in os.listdir(dir_path):
            if filename.endswith(".tf"):
                with open(os.path.join(dir_path, filename), "r") as f:
                    try:
                        parsed = hcl2.load(f)
                        if "locals" in parsed:
                            for local_block in parsed["locals"]:
                                self.locals_cache.update(local_block)
                    except Exception:
                        continue

    def _resolve_tags(self, tags_config: Any) -> Dict[str, Any]:
        """Resolve tags from direct dicts, strings, or merge()"""
        if isinstance(tags_config, dict):
            return tags_config
        if isinstance(tags_config, str):
            if tags_config.startswith("merge("):
                return self._evaluate_merge(tags_config)
            return self._parse_dict(tags_config)
        return {}

    def _evaluate_merge(self, merge_expr: str) -> Dict[str, Any]:
        """Evaluate merge(local.x, local.y, {key=value}) by resolving all references"""
        merged_tags = {}
        # Extract arguments from merge(...)
        args = self._extract_merge_args(merge_expr)
        for arg in args:
            if arg.startswith("local."):
                # Resolve nested locals (e.g., local.tags.cvlt_backup.non_iaas)
                parts = arg.split(".")[1:]  # Skip "local"
                current = self.locals_cache
                try:
                    for part in parts:
                        current = current[part]
                    if isinstance(current, dict):
                        merged_tags.update(current)
                except KeyError:
                    continue
            elif arg.startswith("{"):
                merged_tags.update(self._parse_dict(arg))
        return merged_tags

    def _extract_merge_args(self, merge_expr: str) -> List[str]:
        """Split merge(a,b,c) into ["a", "b", "c"]"""
        inner = merge_expr[6:-1]  # Remove "merge(" and ")"
        args = []
        current = ""
        brace_level = 0
        for char in inner:
            if char == "," and brace_level == 0:
                args.append(current.strip())
                current = ""
            else:
                current += char
                if char in "({[":
                    brace_level += 1
                elif char in ")}]":
                    brace_level -= 1
        if current:
            args.append(current.strip())
        return args

    def _parse_dict(self, dict_str: str) -> Dict[str, str]:
        """Parse {key="value"} or {'key':'value'} into a dict"""
        tags = {}
        try:
            # Extract k=v pairs between {}
            inner = dict_str[1:-1].strip()
            if not inner:
                return tags
            for pair in re.split(r",\s*(?![^{}]*\})", inner):  # Split on commas not inside {}
                if "=" in pair:
                    k, v = map(str.strip, pair.split("=", 1))
                    tags[k.strip('"\'')] = v.strip('"\'')
        except Exception:
            pass
        return tags

check = EnsureTagsExist()


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
