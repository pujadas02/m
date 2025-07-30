## What "Sets the internal DNS setting for new projects to Zonal DNS Only" means:

* This is an **organization-level constraint** that affects **how DNS resolution works for *all VM instances* within new projects** created under that org/folder.
* It sets the **default DNS behavior** for the *project* — specifically, whether VMs use **Zonal DNS** or the default (usually global) DNS.

### What `vmdnssetting` metadata does:

* `vmdnssetting` is a **project-level metadata key** also **instance level** that **enables or controls zonal/global DNS for all VMs in that project** or a **single vm**.



https://cloud.google.com/compute/docs/metadata/predefined-metadata-keys


## 1. Project-level vmdnssetting
Set at the project metadata level.

Controls the default internal DNS behavior for all VM instances in the project.

This is the broad setting that influences how DNS resolution works project-wide.

Setting it here affects all existing and new VMs unless overridden at the instance level.

## 2. Instance-level vmdnssetting
Can be set on individual VM instances.

Overrides the project-level setting for that particular VM.

Useful if you want specific VMs to use different DNS behavior than the project default.

