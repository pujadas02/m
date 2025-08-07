from __future__ import annotations
from typing import Any
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class AllowedExternalIPv4VMCheck(BaseResourceCheck):
    def __init__(self):
        super().__init__(
            name="Ensure external IPv4 only allowed for specified VM instances",
            id="CUSTOM_GCP_001",
            categories=[CheckCategories.NETWORKING],
            supported_resources=["google_compute_instance"],
        )
        # Allowed VM instance names - customize as needed
        self.allowed_vms = {"allowed-vm-1", "allowed-vm-2"}

    def scan_resource_conf(self, conf):
        # Get the VM name; conf attributes are lists in Checkov's parsed format
        vm_name = conf.get("name", [None])[0]
        if not vm_name:
            # No name: cannot verify, pass to avoid false positives
            return CheckResult.PASSED

        # Get list of network_interface blocks
        network_interfaces = conf.get("network_interface", [])
        for ni in network_interfaces:
            # Each network_interface could be list (due to HCL parsing), flatten it
            if isinstance(ni, list):
                ni = ni[0]
            # Check if access_config block(s) exist => external IPv4 assigned
            if "access_config" in ni and ni["access_config"]:
                # VM has external IP, check if allowed
                if vm_name in self.allowed_vms:
                    return CheckResult.PASSED
                else:
                    return CheckResult.FAILED
        # No external IP assigned; safe to pass
        return CheckResult.PASSED

check = AllowedExternalIPv4VMCheck()

# class AllowedExternalIPv4ForVMCheck(BaseResourceCheck):
#     def __init__(self):
#         super().__init__(
#             name="Allowed external IPv4 only for specific VM instances",
#             id="CUSTOM_GCP_001",
#             categories=[CheckCategories.NETWORKING],
#             supported_resources=["google_compute_instance"],
#         )
#         self.allowed_vms = {"allowed-vm-1", "allowed-vm-2"}

#     def scan_resource_conf(self, conf):
#         vm_name = conf.get("name", [None])[0]
#         if not vm_name:
#             return CheckResult.PASSED
        
#         interfaces = conf.get("network_interface", [])
#         for ni in interfaces:
#             if isinstance(ni, list):
#                 ni = ni[0]
#             if "access_config" in ni and ni["access_config"]:
#                 return CheckResult.PASSED if vm_name in self.allowed_vms else CheckResult.FAILED
#         return CheckResult.PASSED

# check = AllowedExternalIPv4ForVMCheck()





# from __future__ import annotations
# from typing import Any
# from checkov.common.models.enums import CheckResult, CheckCategories
# from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

# class AllowedExternalIPv4VMCheck(BaseResourceCheck):
#     def __init__(self):
#         super().__init__(
#             name="Ensure external IPv4 only allowed for specified VM instances",
#             id="CUSTOM_GCP_001",
#             categories=[CheckCategories.NETWORKING],
#             supported_resources=["google_compute_instance"],
#         )
#         # Allowed VM instance names
#         self.allowed_vms = {"allowed-vm-1", "allowed-vm-2"}

#     def scan_resource_conf(self, conf):
#         vm_name = conf.get("name", [None])[0]
#         if not vm_name:
#             # No name given, pass by default or you can adjust logic here
#             return CheckResult.PASSED

#         network_interfaces = conf.get("network_interface", [])
#         for ni in network_interfaces:
#             if isinstance(ni, list):
#                 ni = ni[0]
#             if "access_config" in ni and ni["access_config"]:
#                 # access_config exists with some config: external IP assigned
#                 return CheckResult.PASSED if vm_name in self.allowed_vms else CheckResult.FAILED

#         # No access_config found in any network_interface => no external IP, pass
#         return CheckResult.PASSED

# check = AllowedExternalIPv4VMCheck()
