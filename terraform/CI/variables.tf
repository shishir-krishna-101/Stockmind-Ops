variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "ami_image" {
  description = "ami image name"
  type        = string
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "stockmind"
}

variable "instance_type" {
  description = "CI server EC2 instance type"
  type        = string
  default     = "t3.large"
}

variable "key_name" {
  description = "Existing EC2 key pair name"
  type        = string
}

#variable "allowed_ssh_cidr" {
#  description = "CIDR allowed to SSH to Jenkins"
#  type        = string
#}


