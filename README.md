## What "Sets the internal DNS setting for new projects to Zonal DNS Only" means:

* This is an **organization-level constraint** that affects **how DNS resolution works for *all VM instances* within new projects** created under that org/folder.
* It sets the **default DNS behavior** for the *project* — specifically, whether VMs use **Zonal DNS** or the default (usually global) DNS.

### What `vmdnssetting` metadata does:

* `vmdnssetting` is a **project-level metadata key** also **instance level** that **enables or controls zonal/global DNS for all VMs in that project** or a **single vm**.



https://cloud.google.com/compute/docs/metadata/predefined-metadata-keys
