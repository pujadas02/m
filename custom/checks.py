from checkov.terraform.checks.resource.base_resource_check import BaseResourceValueCheck
from checkov.common.models.enums import CheckCategories, CheckResult

class AllowedExternalIPv4ForVMCheck(BaseResourceValueCheck):
    def __init__(self):
        super().__init__(
            name="Allowed external IPv4 only for specific VM instances",
            id="CUSTOM_GCP_001",
            categories=[CheckCategories.NETWORKING],
            supported_resources=["google_compute_instance"],
        )
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
        return CheckResult.PASSED

check = AllowedExternalIPv4ForVMCheck()
