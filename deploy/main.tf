#------------------------------
# Task:
# 
# Created by Kevin Shindel
#------------------------------

variable "gh_token" {
  type = string
  description = "GitHub token"
}

variable "project_name" {
  type = string
  description = "ProjectName"
}

variable "public_key" {
  type = string
  description = "ssh public key"
}

provider "aws" {
  profile = "default"
}

data "aws_ami" "latest_ubuntu" {
  owners = ["099720109477"]
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

resource "aws_security_group" "this" {
  name = "Military Server"

  dynamic "ingress" {
    for_each = ["80", "443", "22", "8080"]
    content {
      to_port = ingress.value
      from_port = ingress.value
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port = 0
    protocol  = "-1"
    to_port   = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_eip" "this" {
  instance = aws_instance.server.id
}

resource "aws_instance" "server" {
  key_name = aws_key_pair.this.id
  vpc_security_group_ids  = [aws_security_group.this.id]
  ami                     = data.aws_ami.latest_ubuntu.id
  instance_type           = "t2.micro"

  user_data               = templatefile("deploy_script.sh.tpl", {
    project_name = var.project_name
    gh_token = var.gh_token
  })

}

resource "aws_key_pair" "this" {
  key_name   = "aws_key"
  public_key = file(var.public_key)
}

output "instance_public_url" {
  value = aws_eip.this.public_dns
}