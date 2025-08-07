from __future__ import annotations
from typing import Any
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
class AllowedExternalIPv4ForVMCheck(BaseResourceCheck):
    def __init__(self):
        super().__init__(
            name="Allowed external IPv4 only for specific VM instances",
            id="CUSTOM_GCP_001",
            categories=[CheckCategories.NETWORKING],
            supported_resources=["google_compute_instance"],  )
        self.allowed_vms = {"allowed-vm-1", "allowed-vm-2"}
    def scan_resource_conf(self, conf):
        vm_name = conf.get("name", [None])[0]
        if not vm_name:
            return CheckResult.PASSED
        interfaces = conf.get("network_interface", [])
        for ni in interfaces:
            if isinstance(ni, list):
                ni = ni[0]
            if "access_config" in ni and ni["access_config"]:
                return CheckResult.PASSED if vm_name in self.allowed_vms else CheckResult.FAILED
        return CheckResult.SKIPPED
check = AllowedExternalIPv4ForVMCheck()





# from __future__ import annotations

# from typing import Any
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class AllowedExternalIPv4ForVMCheck(BaseResourceCheck):
#     def __init__(self) -> None:
#         name = "Ensure external IPv4 only allowed for specified VM instances"
#         id = "CUSTOM_GCP_001"
#         supported_resources = ['google_compute_instance']
#         categories = [CheckCategories.NETWORKING]
#         super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

#         # Define allowed VM instance names exactly as they appear in Terraform 'name'
#         self.allowed_vms: set[str] = {"allowed-vm-1", "allowed-vm-2"}

#     def scan_resource_conf(self, conf: dict[str, list[Any]]) -> CheckResult:
#         # The VM 'name' attribute is parsed by Checkov as a list (with one str element)
#         vm_names = conf.get("name")
#         if not vm_names or not isinstance(vm_names, list) or not vm_names[0]:
#             # No VM name, unable to validate external IP usage reliably; pass
#             return CheckResult.PASSED
#         vm_name = vm_names[0]

#         # 'network_interface' is a list of blocks (each usually a list with a dict)
#         network_interfaces = conf.get("network_interface", [])
#         for ni in network_interfaces:
#             if isinstance(ni, list) and len(ni) > 0:
#                 ni = ni[0]
#             # Check if access_config block is present and non-empty, meaning external IPv4 enabled
#             access_config = ni.get("access_config")
#             if access_config:
#                 # access_config block exists (ephemeral or static IP assigned)
#                 # Check if VM's name is in allowed list
#                 if vm_name in self.allowed_vms:
#                     return CheckResult.PASSED
#                 else:
#                     return CheckResult.FAILED

#         # No access_config found on any network interface => no external IPv4 assigned => pass
#         return CheckResult.PASSED

# check = AllowedExternalIPv4ForVMCheck()
