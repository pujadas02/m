resource "google_workbench_instance" "example_pass" {
  name = "workbench-instance-pass"
  gce_setup {
    hi = hi
    disable_public_ip = true
    network_interfaces {
      network = "default"
    }
  }
}

resource "google_workbench_instance" "example_fail1" {
  name = "workbench-instance-fail1"
  gce_setup {
    disable_public_ip = false
    network_interfaces {
      network = "default"
    }
  }
}

resource "google_workbench_instance" "example_fail2" {
  name = "workbench-instance-fail2"
  gce_setup {
    disable_public_ip = true
    network_interfaces {
      network = "default"
      access_config {  
      }
    }
  }
}

resource "google_workbench_instance" "example_fail3" {
  name = "workbench-instance-fail3"
  gce_setup {
    disable_public_ip = false
    network_interfaces {
      network = "default"
      access_config {
      }
    }
  }
}



resource "google_compute_network" "vpc_network" {
  project                                   = "my-project-name"
  name                                      = "vpc-network"
  routing_mode                              = "GLOBAL"
  bgp_best_path_selection_mode              = "STANDARD"
}
