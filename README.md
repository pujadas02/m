### Disable Root Access on Vertex AI Workbench Notebooks

This policy enforces `constraints/ainotebooks.disableRootAccess = true`, which blocks users from enabling **root (sudo) access** in new **Vertex AI Workbench user-managed notebooks**.

Internally, the system applies the metadata flag:

```
notebook-disable-root: "true"
```

* 🔒 **Prevents elevation of privileges inside notebook VMs**
* 📊 **Supports security, compliance, and governance controls**
* 🧱 **Helps enforce least-privilege principles in development environments**

**OFFICIAL DOC** – [Manage Metadata on Vertex AI Workbench Instances](https://cloud.google.com/vertex-ai/docs/workbench/instances/manage-metadata)

| Feature     | Metadata Key                   | Value             | Behavior                                     |
| ----------- | ------------------------------ | ----------------- | -------------------------------------------- |
| Root Access | `notebook-disable-root` | `true`            | ✅ Disables sudo/root access in notebooks     |
|             |                                | `false` (default) | ❌ Allows root access in notebook environment |

