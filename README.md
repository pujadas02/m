# 🚫 Disable Terminal Access on Vertex AI Workbench Instances

This policy ensures that terminal access in Vertex AI Workbench notebook instances is **disabled** by enforcing the metadata key:

### Why Disable Terminal Access?

By default, JupyterLab terminals are enabled on Vertex AI Workbench instances, allowing users shell access to the instance environment. While this can be useful, it also increases security risks such as unauthorized access or command execution outside the notebook environment.

Disabling terminal access helps:

* Limit attack surface by blocking shell access.
* Enforce stricter user interaction through notebook UI only.
* Reduce risks of privilege escalation or lateral movement.


## 📋 Enforcement Behavior

| Feature         | Setting                                       | Behavior                                 |
| --------------- | --------------------------------------------- | ---------------------------------------- |
| Terminal Access | `notebook-disable-terminal: "true"`           | ❌ Terminal access disabled in JupyterLab |
| Terminal Access | `notebook-disable-terminal: "false"` or unset | ✅ Terminal access enabled (default)      |

## 📘 References
  [docs](https://cloud.google.com/vertex-ai/docs/workbench/instances/manage-metadata)

## Example: Terraform snippet to create a Notebook instance with terminal disabled

```hcl
resource "google_workbench_instance" "default" {
  name     = "workbench-instance-example"
  location = "us-central1-a"

  gce_setup {
    machine_type = "n1-standard-1"
    vm_image {
      project = "cloud-notebooks-managed"
      family  = "workbench-instances"
    }
    metadata = {
     "notebook-disable-terminal" = "true"
    }
  }
}
```



