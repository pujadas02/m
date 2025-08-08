from __future__ import annotations
from typing import Any
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
class RestrictVmIpForwarding(BaseResourceCheck):
    def __init__(self):
        super().__init__(
            name="Allowed ip forwarding only for specific VM instances",
            id="CUSTOM_GCP_RESTRICT_VM_IP_FORWARDING",
            categories=[CheckCategories.NETWORKING],
            supported_resources=["google_compute_instance"],  )
        self.allowed_vms = {"allowed-vm-1", "allowed-vm-2"}
    def scan_resource_conf(self, conf):
        vm_name = conf.get("name", [None])[0]
        if not vm_name:
            return CheckResult.SKIPPED
        can_ip_forward = conf.get("can_ip_forward")
        if not can_ip_forward or not isinstance(can_ip_forward, list):
            return CheckResult.SKIPPED
        if can_ip_forward[0] is True:
            return CheckResult.PASSED if vm_name in self.allowed_vms else CheckResult.FAILED
        return CheckResult.SKIPPED
check = RestrictVmIpForwarding()
