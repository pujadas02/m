from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class OSLoginEvaluator(BaseResourceCheck):
    def __init__(self):
        name = "Validate OS Login setting between project and instances"
        id = "CUSTOM_GCP_OSLOGIN_LOGIC_TREE_1"
        supported_resources = [
            "google_compute_project_metadata",
            "google_compute_instance",
        ]
        categories = [CheckCategories.IAM]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

        self.project_metadata = None  # store one project metadata config
        self.vm_instances = []        # store all VM metadata blocks

    def scan_resource_conf(self, conf):
        resource_type = conf.get("__tfmeta__", {}).get("resource_type")

        if resource_type == "google_compute_project_metadata":
            self.project_metadata = conf.get("metadata", [{}])[0]
            return CheckResult.UNKNOWN  # delay decision

        if resource_type == "google_compute_instance":
            metadata = conf.get("metadata", [{}])[0]
            self.vm_instances.append(metadata)
            return CheckResult.UNKNOWN  # delay decision

        return CheckResult.UNKNOWN

    def after_scan(self, results):
        """
        This runs after all resources are scanned — apply the logic here.
        """
        evaluations = []

        project_has_oslogin = False
        if self.project_metadata:
            project_has_oslogin = (
                self.project_metadata.get("enable-oslogin", "").lower() == "true"
            )

        for vm_metadata in self.vm_instances:
            vm_has_oslogin = "enable-oslogin" in vm_metadata
            vm_oslogin_value = vm_metadata.get("enable-oslogin", "").lower()

            # Rule 1: project has enable-oslogin=true, VM may or may not set it
            if project_has_oslogin:
                if not vm_has_oslogin or vm_oslogin_value == "true":
                    evaluations.append(CheckResult.PASSED)
                else:
                    evaluations.append(CheckResult.FAILED)

            # Rule 2: project metadata exists but enable-oslogin is NOT true
            elif self.project_metadata:
                # VM must NOT override it (i.e. must not set it)
                if not vm_has_oslogin:
                    evaluations.append(CheckResult.PASSED)
                else:
                    evaluations.append(CheckResult.FAILED)

            # Rule 3: project metadata doesn't exist
            else:
                # VM must explicitly set enable-oslogin = true
                if vm_oslogin_value == "true":
                    evaluations.append(CheckResult.PASSED)
                else:
                    evaluations.append(CheckResult.FAILED)

        # Overall: if all VMs passed, success
        if all(result == CheckResult.PASSED for result in evaluations):
            return CheckResult.PASSED
        return CheckResult.FAILED

check = OSLoginEvaluator()
