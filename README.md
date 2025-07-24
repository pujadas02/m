### Disable File Downloads on Vertex AI Workbench Notebooks

This policy enforces **`constraints/ainotebooks.disableFileDownloads = true`**, which blocks users from enabling the file download option in the Vertex AI Workbench UI. Internally, the system applies the metadata flag:  
```yaml
notebook-disable-downloads: "true"

```
Prevents sensitive data exfiltration from notebooks

Supports compliance and data governance requirements

Helps maintain a secure environment by blocking unsafe downloads

OFFICIAL DOC - https://cloud.google.com/vertex-ai/docs/workbench/instances/manage-metadata
