## Use Compute Engine Service Account by Default (Cloud Build)	This boolean constraint, when enforced, allows the Compute Engine service account to be used by default.

## The default Compute Engine service account is created automatically by Google Cloud when you first enable the Compute Engine API in your project.

**If policy is enforced (true):**
When no service account is specified explicitly in the Cloud Build config, Cloud Build will use the Compute Engine default service account automatically by default.

**If policy is disabled or unset (false):**
When no service account is specified, Cloud Build will NOT use the Compute Engine default service account automatically.

**Important nuance:**
This policy controls only the automatic default usage of the Compute Engine default service account.

It does NOT prevent you from explicitly specifying the Compute Engine service account as a custom service account in your build config.

So, even if the policy is disabled, you can still specify the Compute Engine default service account explicitly and Cloud Build will use it.
