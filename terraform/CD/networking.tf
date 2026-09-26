locals {
  azs = var.availability_zones

  public_subnets = [
    for i, az in local.azs : cidrsubnet(var.vpc_cidr, 8, i)
  ]

  private_subnets = [
    for i, az in local.azs : cidrsubnet(var.vpc_cidr, 8, i + 10)
  ]

  database_subnets = [
    for i, az in local.azs : cidrsubnet(var.vpc_cidr, 8, i + 20)
  ]
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "6.6.0"

  name = "${var.project_name}-${var.environment}-vpc"
  cidr = var.vpc_cidr

  azs = local.azs

  public_subnets   = local.public_subnets
  private_subnets  = local.private_subnets
  database_subnets = local.database_subnets

  enable_nat_gateway = true
  single_nat_gateway = true

  enable_dns_hostnames = true
  enable_dns_support   = true

  public_subnet_tags = {
    "kubernetes.io/role/elb" = "1"
  }

  private_subnet_tags = {
    "kubernetes.io/role/internal-elb" = "1"
  }

  tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}
