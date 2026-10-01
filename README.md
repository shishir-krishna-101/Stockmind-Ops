# StockMind Ops

StockMind is an AI-assisted inventory-management and inventory-intelligence application designed to help businesses understand demand, identify low-stock situations, forecast futures, and provide useful inventory recommendations.

This repository (`Stockmind-Ops`) contains the Terraform foundations and DevOps environment for the platform.

**Note:** The application source code (React frontend, FastAPI backend) is maintained in a separate repository: `https://github.com/shishir-krishna-101/StockMind.git`

## Current Status
**The project is still being built.** Currently, Terraform is the primary implemented DevOps component. The full CI/CD pipeline, GitOps deployment, and observability stack are planned.

## Architecture Design

The diagram below shows the intended target architecture. The project is currently at the Terraform stage.

![StockMind DevOps architecture design](src/Images/Stock_mind_Architecture.png)

## Technology Overview
- **Application:** React (Frontend), FastAPI (Backend), PostgreSQL, Gemini API (AI — Planned)
- **Infrastructure:** Terraform, AWS (VPC, EKS, RDS, ECR, EC2)
- **Configuration Management (Planned):** Ansible — manages the Jenkins EC2 CI server configuration (plugins, tool upgrades, hardening) after Terraform provisions it
- **CI/CD (Planned):** Jenkins, SonarQube, Trivy, Cosign, Argo CD
- **Observability (Planned):** Prometheus, Grafana, Fluent Bit, Loki, OpenTelemetry, Tempo, Alertmanager

## Repository Structure
```text
terraform/
  CI/       # Jenkins EC2 host and ECR foundations
  CD/       # AWS EKS, RDS, networking, and Argo CD bootstrap
ansible/    # Configuration management for CI EC2 server (PLANNED)
docs/       # Comprehensive project documentation
```

## Terraform Quick Start
Navigate to `terraform/CI` or `terraform/CD`. Copy `terraform.tfvars.example` to `terraform.tfvars` and run:
```powershell
terraform init
terraform plan
terraform apply
```
*Do not commit your `terraform.tfvars` file.*

## Comprehensive Documentation
For a complete understanding of the architecture, decisions, security, and cost models, please read the documentation:

[**📖 View Master Documentation**](docs/README.md)

### Key Documentation Links
- [Current Status Matrix](docs/STATUS.md)
- [Roadmap & Changelog](docs/CHANGELOG.md)
- [Application Architecture](docs/02-architecture/README.md)
- [AWS & Terraform](docs/03-aws/README.md)
- [CI/CD & GitOps](docs/07-cicd/README.md)
- [Cost Model](docs/13-cost/README.md)
- [Security Overview](docs/10-security/README.md)
- [Architecture Decisions (ADRs)](docs/14-decisions/README.md)
