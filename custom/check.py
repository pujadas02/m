from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class OSLoginEnforcedProjectOrInstance(BaseResourceCheck):
    def __init__(self):
        name = "Ensure OS Login is enabled on project or instance level"
        id = "CUSTOM_GCP_OSLOGIN"
        supported_resources = ["google_compute_project_metadata", "google_compute_instance"]
        categories = [CheckCategories.IAM]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
        self.project_oslogin_enabled = None  # to track project metadata globally

    def scan_resource_conf(self, conf):
        # Project metadata check
        if self.entity_type == "google_compute_project_metadata":
            metadata = conf.get("metadata", [{}])[0]
            oslogin = metadata.get("enable-oslogin")
            if oslogin and str(oslogin).upper() == "TRUE":
                self.project_oslogin_enabled = True
                return CheckResult.PASSED
            else:
                self.project_oslogin_enabled = False
                return CheckResult.FAILED

        # Instance metadata check
        if self.entity_type == "google_compute_instance":
            metadata = conf.get("metadata", [{}])[0]
            oslogin = metadata.get("enable-oslogin")

            # Case: project-level metadata is not available
            if self.project_oslogin_enabled is None:
                if oslogin and str(oslogin).upper() == "TRUE":
                    return CheckResult.PASSED
                else:
                    return CheckResult.FAILED

            # Case: project-level metadata exists and is valid
            if self.project_oslogin_enabled:
                if oslogin is None or str(oslogin).upper() == "TRUE":
                    return CheckResult.PASSED
                else:
                    return CheckResult.FAILED

            # Case: project-level metadata exists but is invalid
            return CheckResult.FAILED

        return CheckResult.UNKNOWN


check = OSLoginEnforcedProjectOrInstance()
