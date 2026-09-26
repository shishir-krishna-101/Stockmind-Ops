module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "6.6.0"

  name = "stockmind-ci-vpc"
  cidr = "10.1.0.0/16"

  azs            = ["ap-south-1a"]
  public_subnets = ["10.1.1.0/24"]

  enable_nat_gateway = false

  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "stockmind-ci-vpc"
    Environment = "dev"
    Purpose     = "CI"
  }
}




# STEP 0: CREATE VPC AND SUBNET
resource "aws_vpc" "jenkins-vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = {
    Name = "JENKINS-VPC"
  }
}

resource "aws_subnet" "jenkins-subnet" {
  vpc_id                  = aws_vpc.jenkins-vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "${var.region_name}"
  tags = {
    Name = "JENKINS-SUBNET"
  }
}
