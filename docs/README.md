# StockMind Documentation

Welcome to the StockMind documentation. StockMind is an AI-assisted inventory-management / inventory-intelligence application.

## Business Purpose
StockMind turns raw inventory and sales data into actionable business insights, dashboards, alerts, forecasts, and recommendations, using AI to identify low-stock situations and forecast demand.

## Current Status
**The project is still being built.** Currently, Terraform is the primary implemented DevOps component. The application (React, FastAPI, PostgreSQL) and future AI operations engine are either implemented in a separate application repository or planned. See [STATUS.md](STATUS.md) for a detailed matrix.

## Architecture Image
![StockMind DevOps architecture design](../src/Images/Stock_mind_Architecture.png)

## Technology Overview
- **Application:** React (Frontend), Python/FastAPI (Backend), PostgreSQL (Database), Google Gemini API (AI - Planned).
- **Infrastructure:** AWS (EKS, EC2, ECR, RDS, VPC), Terraform (IaC).
- **CI/CD (Planned):** Jenkins, SonarQube, Trivy, Cosign, Argo CD (GitOps).
- **Observability (Planned):** Prometheus, Grafana, Fluent Bit, Loki, OpenTelemetry, Tempo, Alertmanager.

## Repository Structure
This repository (`Stockmind-Ops`) contains the infrastructure components.
- `terraform/CI/`: Jenkins EC2 host and ECR foundations (Implemented)
- `terraform/CD/`: AWS EKS, RDS, networking, and Argo CD bootstrap (Implemented)
- `docs/`: Comprehensive project documentation.

The application code is in a separate repository: `https://github.com/shishir-krishna-101/StockMind.git`

## Terraform Quick Start
Navigate to `terraform/CI/` or `terraform/CD/`, copy `terraform.tfvars.example` to `terraform.tfvars` (do not commit), and run:
```bash
terraform init
terraform plan
terraform apply
```

## Documentation Index
1. [Project Overview](01-overview/README.md)
2. [Application Architecture](02-architecture/README.md)
3. [AWS Architecture](03-aws/README.md)
4. [Networking](04-networking/README.md)
5. [Terraform](05-terraform/README.md)
6. [Kubernetes](06-kubernetes/README.md)
7. [CI/CD](07-cicd/README.md)
8. [GitOps](08-gitops/README.md)
9. [Observability](09-observability/README.md)
10. [Security](10-security/README.md)
11. [AI Incident Engine](11-ai-incident-engine/README.md)
12. [Operations](12-operations/README.md)
13. [Cost](13-cost/README.md)
14. [Architecture Decisions (ADRs)](14-decisions/)

## Roadmap & Cost Model
- [Roadmap (CHANGELOG.md)](CHANGELOG.md)
- [Cost Model](13-cost/README.md)

## Security Overview
Security is integrated at multiple layers: IAM Roles for least privilege, Security Groups avoiding `0.0.0.0/0` for internals, Trivy/Cosign in the CI pipeline (planned), and a strict safety model for the future AI Incident Engine. See [Security](10-security/README.md) for details.
