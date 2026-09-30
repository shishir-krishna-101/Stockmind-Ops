from scratch_gen_docs_helper import write_doc, tech_template

readme_content = """# StockMind Documentation

Welcome to the StockMind documentation. StockMind is an AI-assisted inventory-management / inventory-intelligence application.

## Business Purpose
StockMind turns raw inventory and sales data into actionable business insights, dashboards, alerts, forecasts, and recommendations, using AI to identify low-stock situations and forecast demand.

## Current Status
**The project is still being built.** Currently, Terraform is the primary implemented DevOps component. The application (React, FastAPI, PostgreSQL) and future AI operations engine are either implemented in a separate application repository or planned. See [STATUS.md](STATUS.md) for a detailed matrix.

## Architecture Image
![StockMind DevOps architecture design](../src/Images/Stock_mind_Architecture.png)

## Technology Overview
- **Application:** React (Frontend), Python/FastAPI (Backend), PostgreSQL (Database), Google Gemini API (AI).
- **Infrastructure:** AWS (EKS, EC2, ECR, RDS, VPC), Terraform (IaC).
- **CI/CD (Planned):** Jenkins, SonarQube, Trivy, Cosign, Argo CD (GitOps).
- **Observability (Planned):** Prometheus, Grafana, Fluent Bit, Loki, OpenTelemetry, Tempo, Alertmanager.

## Repository Structure
This repository (`Stockmind-Ops`) contains the infrastructure components.
- `terraform/CI/`: Jenkins EC2 host and ECR foundations (Implemented)
- `terraform/CD/`: AWS EKS, RDS, networking, and Argo CD bootstrap (Implemented)
- `docs/`: Comprehensive project documentation.

The application code is in a separate repository: `https://github.com/Harshuqt/StockMind.git`

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
"""

status_content = """# CURRENT / PLANNED / HISTORICAL MATRIX

## Application
- **React**: CURRENT (in application repo)
- **FastAPI**: CURRENT (in application repo)
- **PostgreSQL**: CURRENT (in application repo)
- **JWT**: CURRENT (in application repo)
- **SQLAlchemy**: CURRENT (in application repo)
- **Alembic**: CURRENT (in application repo)
- **Gemini**: CURRENT (in application repo, application AI)

## Infrastructure
- **Terraform**: CURRENT (IMPLEMENTED)
- **AWS**: CURRENT (IMPLEMENTED)
- **VPC**: CURRENT (IMPLEMENTED)
- **EC2**: CURRENT (IMPLEMENTED)
- **ECR**: CURRENT (IMPLEMENTED)
- **EKS**: CURRENT (IMPLEMENTED)
- **RDS**: CURRENT (IMPLEMENTED)
- **IAM**: CURRENT (IMPLEMENTED)
- **Security Groups**: CURRENT (IMPLEMENTED)

## CI (Continuous Integration)
- **Jenkins**: PLANNED (EC2 foundation exists, pipeline pending)
- **SonarQube**: PLANNED
- **Trivy**: PLANNED
- **Cosign**: PLANNED

## CD (Continuous Deployment)
- **Argo CD**: PARTIALLY IMPLEMENTED (Bootstrap installed via Terraform, GitOps apps pending)

## Observability
- **Prometheus**: PLANNED
- **Grafana**: PLANNED
- **Fluent Bit**: PLANNED
- **Loki**: PLANNED
- **OpenTelemetry**: PLANNED
- **Tempo**: PLANNED
- **Alertmanager**: PLANNED

## Advanced
- **Istio**: PLANNED
- **AI Incident Engine**: PLANNED (Future operations feature)
- **Human-approved remediation**: PLANNED

## Historical/Removed
- **Redis**: HISTORICAL/REMOVED (Not being used, removed to simplify architecture)
- **Karpenter**: HISTORICAL/REMOVED (Replaced with managed node groups for current scale)
- **Ansible core approach**: HISTORICAL/REMOVED (Using Terraform and GitOps instead)
- **Route 53 core requirement**: HISTORICAL/REMOVED
"""

changelog_content = """# Roadmap and Changelog

## Phase 1: Terraform foundation
**Goal:** Establish AWS networking, EKS, RDS, CI host, and ECR using Terraform.
**Dependencies:** AWS account, Terraform CLI.
**Implementation tasks:** Write VPC, IAM, EKS, RDS, EC2, ECR terraform modules.
**Definition of Done:** Infrastructure applies successfully without errors.
**Risks:** Misconfigured security groups, state loss.
**Cost implications:** EKS control plane cost, EC2 instance cost, RDS hourly costs.
**Documentation required:** ADRs for AWS, EKS, RDS.
**Status:** IMPLEMENTED.

## Phase 2: Application containerization
**Goal:** Create robust Dockerfiles for frontend and backend.
**Dependencies:** Phase 1.
**Implementation tasks:** Multi-stage builds, non-root users.
**Definition of Done:** Images build and run locally.
**Risks:** Large image sizes.
**Cost implications:** Storage costs in ECR.
**Documentation required:** Docker architecture.
**Status:** CURRENT (in app repo).

## Phase 3: AWS/EKS deployment
**Goal:** Deploy initial workloads to EKS manually or via basic manifests.
**Dependencies:** Phase 1, Phase 2.
**Implementation tasks:** K8s Deployments, Services, Ingress.
**Definition of Done:** App accessible via ALB.
**Risks:** Load balancer controller misconfiguration.
**Cost implications:** ALB hourly costs.
**Documentation required:** K8s architecture.
**Status:** PLANNED.

## Phase 4: Jenkins CI
**Goal:** Automate builds and tests on Jenkins EC2 host.
**Dependencies:** Phase 1, Phase 2.
**Implementation tasks:** Jenkinsfile, webhook setup.
**Definition of Done:** Commits trigger build/test.
**Risks:** Jenkins security, flaky tests.
**Cost implications:** Jenkins EC2 ongoing cost.
**Documentation required:** CI diagram.
**Status:** PLANNED.

## Phase 5: Security scanning/signing
**Goal:** Integrate Trivy and Cosign into Jenkins pipeline.
**Dependencies:** Phase 4.
**Implementation tasks:** Add scanning stages to Jenkinsfile.
**Definition of Done:** Images scanned and signed before pushing to ECR.
**Risks:** Build time increases, false positives.
**Cost implications:** KMS signing key costs (if applicable).
**Documentation required:** ADR for security scanning.
**Status:** PLANNED.

## Phase 6: Argo CD GitOps
**Goal:** Shift deployment from manual/Jenkins to Argo CD syncing a GitOps repo.
**Dependencies:** Phase 1 (Argo CD bootstrap), Phase 5.
**Implementation tasks:** Create Argo Applications, define GitOps structure.
**Definition of Done:** Argo CD manages frontend/backend deployments automatically.
**Risks:** Sync loops, credential management.
**Cost implications:** Negligible (runs inside EKS).
**Documentation required:** GitOps ADR, flow diagram.
**Status:** PLANNED.

## Phase 7: Observability
**Goal:** Deploy Prometheus, Grafana, Fluent Bit, Loki, OTel, Tempo.
**Dependencies:** Phase 6 (deployed via Argo CD).
**Implementation tasks:** Helm charts in GitOps for observability stack.
**Definition of Done:** Dashboards show metrics, logs queryable in Loki.
**Risks:** High resource usage by observability stack.
**Cost implications:** EKS node scaling, EBS volume costs for storage.
**Documentation required:** Observability ADR, diagram.
**Status:** PLANNED.

## Phase 8: Reliability/autoscaling
**Goal:** Implement HPA/VPA and cluster autoscaling.
**Dependencies:** Phase 7 (Metrics server/Prometheus).
**Implementation tasks:** Configure autoscalers based on CPU/Memory.
**Definition of Done:** Pods and nodes scale up/down under load.
**Risks:** Thrashing, stateful set disruptions.
**Cost implications:** Variable EC2 costs based on load.
**Documentation required:** Reliability runbook.
**Status:** PLANNED.

## Phase 9: Security hardening
**Goal:** Network policies, Istio service mesh.
**Dependencies:** Phase 6, Phase 8.
**Implementation tasks:** Deploy Istio, write deny-all network policies.
**Definition of Done:** mTLS enforced, pod-to-pod traffic restricted.
**Risks:** Breaking app connectivity.
**Cost implications:** Slight overhead in resource usage.
**Documentation required:** Security ADR.
**Status:** PLANNED.

## Phase 10: AI Incident Engine
**Goal:** Deploy the backend service that consumes observability data for RCA.
**Dependencies:** Phase 7, Phase 9.
**Implementation tasks:** Write Engine service, integrate with Gemini/LLM, deploy.
**Definition of Done:** Engine generates RCA reports for alerts.
**Risks:** Hallucinations, slow response times.
**Cost implications:** LLM API usage costs.
**Documentation required:** AI Incident Engine architecture.
**Status:** PLANNED.

## Phase 11: Controlled remediation
**Goal:** Allow AI to suggest and execute allowlisted actions after human approval.
**Dependencies:** Phase 10.
**Implementation tasks:** Approval UI, restricted RBAC for executor.
**Definition of Done:** AI suggests restart, human clicks approve, pod restarts.
**Risks:** Accidental destructive actions if RBAC is too loose.
**Cost implications:** Negligible.
**Documentation required:** AI Safety model documentation.
**Status:** PLANNED.

## Phase 12: Cost optimization
**Goal:** Review and optimize cloud spend.
**Dependencies:** All phases.
**Implementation tasks:** Right-sizing, reserved instances, lifecycle policies.
**Definition of Done:** Cloud bill reduced by targeted percentage.
**Risks:** Under-provisioning.
**Cost implications:** REDUCTION in costs.
**Documentation required:** Cost optimization report.
**Status:** PLANNED.
"""

overview_content = """# 01 - Project Overview

StockMind is an AI-assisted inventory-management / inventory intelligence application.

## 1. What is StockMind?
A full-stack application backed by modern DevOps practices, providing businesses with visibility into their inventory, low-stock detection, demand prediction, and stockout-risk analysis.

## 2. Why does StockMind exist?
1. To solve the business problem of turning raw inventory/sales data into actionable insights and forecasts.
2. To serve as a realistic platform for demonstrating practical cloud infrastructure, containerization, Infrastructure-as-Code (Terraform), CI/CD, GitOps, observability, and advanced AI-assisted operations.

## 3. Two-Repository Model
The project enforces a strict separation of concerns:
- **Application Repository** (`https://github.com/Harshuqt/StockMind.git`): Contains the React frontend, FastAPI backend, and application-level tests.
- **DevOps Repository** (`Stockmind-Ops`): Contains the Terraform AWS infrastructure, Argo CD bootstrapping, CI configuration, and this documentation.

This separation ensures that developers focus on application logic while platform engineers manage infrastructure state without cross-contamination of secrets or concerns.
"""

arch_content = """# 02 - Application Architecture

```mermaid
flowchart LR
    User[User's browser] --> Frontend[React & TypeScript SPA]
    Frontend -->|HTTP/JSON| API[FastAPI REST API]
    API --> ORM[SQLAlchemy async]
    ORM --> DB[(PostgreSQL)]
    API -. Optional AI requests .-> Gemini[Google Gemini API]
```

""" + tech_template("React (Frontend)", 
    "A JavaScript library for building user interfaces.",
    "Provides a dynamic, responsive SPA for inventory management dashboards and workflows.",
    "User-facing frontend.",
    "CURRENT",
    "Industry standard, large ecosystem, component-based.",
    "Vue, Angular, Svelte",
    "React was preferred for its vast ecosystem and existing familiarity.",
    "Client-side rendering can impact initial load time without SSR.",
    "No direct database access; must rely on secure backend APIs.",
    "Requires build pipelines (npm, Vite); adds complexity.",
    "Negligible (served as static files).",
    "Reconsider if SEO becomes critical (move to Next.js) or if UI complexity demands a different paradigm.",
    "Rewriting the UI layer in Vue or Svelte, setting up new build tools."
) + tech_template("FastAPI (Backend)",
    "A modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.",
    "Provides high-performance async REST endpoints, request validation, and OpenAPI documentation.",
    "Core backend service handling business logic and DB communication.",
    "CURRENT",
    "High performance (asyncio), automatic Swagger docs, Pydantic integration.",
    "Django, Flask, Express.js",
    "Django was too heavy; Flask lacks async/validation out-of-the-box; Express changes language stack.",
    "Requires understanding of async Python; smaller ecosystem than Django.",
    "Input validation is robust via Pydantic, reducing injection risks.",
    "Requires ASGI server (Uvicorn) for execution.",
    "EC2/EKS compute costs for running the container.",
    "Reconsider if the application requires heavy monolithic features (like an integrated admin panel) where Django excels.",
    "Migrating routes to Flask or Django, refactoring validation logic."
)

aws_content = """# 03 - AWS Architecture

```mermaid
flowchart TD
    Internet((Internet)) --> IGW[Internet Gateway]
    IGW --> ALB[Application Load Balancer]
    ALB --> EKS[Amazon EKS]
    
    subgraph VPC [AWS VPC]
        subgraph Public Subnet
            NAT[NAT Gateway]
        end
        subgraph Private Subnets
            EKS
            RDS[(Amazon RDS PostgreSQL)]
            CI[Jenkins EC2]
        end
    end
    
    EKS --> NAT
    EKS --> RDS
    
    ECR[Amazon ECR]
    EKS -. pull images .-> ECR
    CI -. push images .-> ECR
```

""" + tech_template("Amazon Web Services (AWS)",
    "A comprehensive, evolving cloud computing platform provided by Amazon.",
    "Provides the scalable infrastructure (compute, network, storage, DB) required to host StockMind.",
    "Underlying cloud provider for the entire platform.",
    "IMPLEMENTED",
    "Market leader, robust managed services (EKS, RDS), excellent Terraform support.",
    "Google Cloud Platform (GCP), Microsoft Azure",
    "Familiarity and specific ecosystem tools (like AWS Load Balancer Controller).",
    "Vendor lock-in, complex pricing model.",
    "Robust IAM and security groups provide strong defense-in-depth, but misconfiguration is a major risk.",
    "Requires high operational maturity to manage correctly.",
    "Can be expensive if resources (like NAT Gateways and EKS control planes) are left running unused.",
    "Reconsider if costs become prohibitive or a multi-cloud strategy is mandated.",
    "Complete infrastructure rewrite for Azure/GCP in Terraform; migrating data from RDS."
)

write_doc("README.md", readme_content)
write_doc("STATUS.md", status_content)
write_doc("CHANGELOG.md", changelog_content)
write_doc("01-overview/README.md", overview_content)
write_doc("02-architecture/README.md", arch_content)
write_doc("03-aws/README.md", aws_content)

print("Batch 1 written.")
