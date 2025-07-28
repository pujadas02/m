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
     "notebook-disable-terminal" = "false"
    }
  }
}
