provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "example" {
  name        = "example-sg"
  description = "Allow inbound traffic on port 80"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Open to the world (this is insecure)
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
