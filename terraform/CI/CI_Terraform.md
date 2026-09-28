# StockMind - Simple CI Terraform

This folder creates only the CI environment.

## What it creates

- 1 EC2 instance for CI tools
- Jenkins
- Java 21
- Docker
- Docker Compose
- Trivy
- Cosign
- AWS CLI
- kubectl
- Helm
- SonarQube as a Docker container
- 3 private ECR repositories
- IAM role allowing the CI server to push images to those ECR repositories
- Security group for SSH, Jenkins, and SonarQube

## Architecture

GitHub
  |
  v
Jenkins EC2
  |
  +-- SonarQube
  +-- Trivy
  +-- Cosign
  +-- Docker
  |
  v
Amazon ECR

## Before terraform apply

1. Create an AWS VPC and subnet, or use an existing one.
2. Create an EC2 key pair.
3. Copy `terraform.tfvars.example` to `terraform.tfvars`.
4. Put your real VPC ID, subnet ID, key pair name, and public IP.

## Deploy

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

## After deployment

Get the URLs:

```bash
terraform output
```

Open Jenkins on port 8080 and SonarQube on port 9000.

Get the initial Jenkins password:

```bash
ssh -i YOUR_KEY.pem ec2-user@<CI_PUBLIC_IP>
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

## Important

This is intentionally a simple CI setup for learning and portfolio use.

The CD/EKS infrastructure is NOT included here. It will be created separately.

For a production setup, Jenkins and SonarQube should normally not share one small server, and secrets/state should be managed more carefully.
