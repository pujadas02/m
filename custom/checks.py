# from __future__ import annotations
# import requests
# import re
# from typing import Any, Dict
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
 
# class EnsureSnapshotLifetimeTagExistsCheck(BaseResourceCheck):
#     def __init__(self) -> None:
#         # name = "Ensure business_criticality tag exists. Valid Values are [A+, a+,A,B,b,C,c,z,z,Tier 0,tier0,T0,tier 0,tier0,t0,Tier 1,Tier1,T1,tier 1,tier1,t1,N/A,NA]"
#         # id = "CCOE_AZ2_TAGS_6"
#         # categories = [CheckCategories.CONVENTION]
#         # supported_resources = ['azurerm_*']
#         # super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
#         # self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"
#         # self.required_tags = {"app", "app_owner_group", "ppm_io_cc", "ppm_id_owner", "expert_centre", "cvlt_backup"}
#         super().__init__(
#             name="Ensure required tags exist",
#             id="CCOE_AZ2_TAGS_6",
#             categories=[CheckCategories.CONVENTION],
#             supported_resources=['azurerm_*']
#         )
#         self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"
#         self.required_tags = {"app", "app_owner_group", "ppm_io_cc", "ppm_id_owner", "expert_centre", "cvlt_backup"}


#     # def has_tags_support(self, resource_type: str) -> bool:
#     #     try:
#     #         response = requests.get(f"{self.docs_url}{resource_type}.html.markdown", timeout=3)
#     #         return response.status_code == 200 and "`tags`" in response.text
#     #     except:
#     #         return False
 
#     def get_tags(self, conf: Dict[str, Any]) -> Dict[str, Any]:
#         tags_config = conf.get("tags", [{}])[0]
#         if isinstance(tags_config, dict):
#             return tags_config
#         if isinstance(tags_config, str):
#             return {k: v for m in re.finditer(r'"(\w*)"\s*:\s*"([^"]*)"', tags_config)
#                     for k, v in [m.groups()]}
#         return {}
 
#     def scan_resource_conf(self, conf: Dict[str, Any]) -> CheckResult:
#         # if not (address := conf.get("__address__", "")):
#         #     return CheckResult.SKIPPED
 
#         # resource_type = address.split(".")[0][8:] 
#         # if not self.has_tags_support(resource_type):
#         #     return CheckResult.SKIPPED

#         if not conf.get("__address__"):
#             return CheckResult.SKIPPED
#         tags = self.get_tags(conf)
#         return CheckResult.PASSED if all(tag in tags for tag in self.required_tags) else CheckResult.FAILED

#         # tags = self.get_tags(conf)   
#         # business_criticality = tags.get("business_criticality")
#         # if business_criticality is not None and business_criticality in [
#         #     "A+", "a+", "A", "a", "B", "b", "C", "c", "Z", "z",
#         #     "Tier 0", "Tier0", "T0", "tier 0", "tier0", "t0",
#         #     "Tier 1", "Tier1", "T1", "tier 1", "tier1", "t1",
#         #     "N/A", "NA"]:
#         #     return CheckResult.PASSED
            
#         # return CheckResult.FAILED
 
# check = EnsureSnapshotLifetimeTagExistsCheck()














from __future__ import annotations
import requests
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
        self.docs_url = "https://raw.githubusercontent.com/hashicorp/terraform-provider-azurerm/main/website/docs/r/"

    def has_tags_support(self, resource_type: str) -> bool:
        try:
            response = requests.get(f"{self.docs_url}{resource_type}.html.markdown", timeout=3)
            return response.status_code == 200 and "`tags`" in response.text
        except:
            return False
 
    def get_tags(self, conf: Dict[str, Any]) -> Dict[str, Any]:
        tags_config = conf.get("tags", [{}])[0]
        if isinstance(tags_config, dict):
            return tags_config
        if isinstance(tags_config, str):
            return {k: v for m in re.finditer(r"'(\w+)'\s*:\s*'([^']*)'", tags_config) 
                   for k, v in [m.groups()]}
        return {}

    def scan_resource_conf(self, conf: Dict[str, Any]) -> CheckResult:
         if not (address := conf.get("__address__", "")):
            return CheckResult.SKIPPED
 
        resource_type = address.split(".")[0][8:] 
        if not self.has_tags_support(resource_type):
            return CheckResult.SKIPPED
         
        # if not conf.get("__address__"):
        #     return CheckResult.SKIPPED
            
        tags = self.get_tags(conf)
     
        business_criticality = tags.get("business_criticality")
        if business_criticality is not None and business_criticality in [
            "A+", "a+", "A", "a", "B", "b", "C", "c", "Z", "z",
            "Tier 0", "Tier0", "T0", "tier 0", "tier0", "t0",
            "Tier 1", "Tier1", "T1", "tier 1", "tier1", "t1",
            "N/A", "NA"]:
            return CheckResult.PASSED
       
        return CheckResult.FAILED
check = EnsureTagsExist()









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
#         self.required_tags = {"app", "app_owner_group", "ppm_io_cc", "ppm_id_owner", "expert_centre", "cvlt_backup"}

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
