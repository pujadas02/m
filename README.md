## What "Sets the internal DNS setting for new projects to Zonal DNS Only" means:

* This is an **organization-level constraint** that affects **how DNS resolution works for *all VM instances* within new projects** created under that org/folder.
* It sets the **default DNS behavior** for the *project* — specifically, whether VMs use **Zonal DNS** or the default (usually global) DNS.

### What `vmdnssetting` metadata does:

* `vmdnssetting` is a **project-level metadata key** that **enables or controls zonal/global DNS for all VMs in that project**.
* DNS resolution itself happens **at the VM (instance) level** because that's where the networking stack uses DNS.
* You **cannot** set DNS mode per individual VM (there’s no VM instance metadata key for this) — it’s a project-wide setting.

### Your summary question:

> *"For new projects here but I am only doing for VM instance here, right? As we can only set DNS setting or DNS is only used in VM instances?"*

* The **DNS setting applies at the project level (via `vmdnssetting`) and affects all VMs** in the project.
* The **actual DNS resolution happens on VMs**, but you don’t set DNS mode individually on VMs.
* So when you set `vmdnssetting` at the project metadata, you control how **all VMs in that project** resolve internal DNS.

### TL;DR:

* The org policy sets the default for new projects.
* `vmdnssetting` is how you implement/control that behavior on an existing project.
* DNS is *used* on VMs but *controlled* at the project level.
* You **cannot** set DNS mode per VM individually.
