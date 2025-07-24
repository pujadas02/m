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
      notebook-disable-downloads = "false"
    }
  }
}

resource "google_vertex_ai_endpoint_with_model_garden_deployment" "deploy" {
  publisher_model_name = "publishers/google/models/paligemma@paligemma-224-float32"
  location             = "us-central1"
  model_config {
    accept_eula =  true
  }
}

data "google_project" "project" {}
