# CURRENT / PLANNED / HISTORICAL MATRIX

## Application
- **React**: CURRENT (in application repo)
- **FastAPI**: CURRENT (in application repo)
- **PostgreSQL**: CURRENT (in application repo)
- **JWT**: CURRENT (in application repo)
- **SQLAlchemy**: CURRENT (in application repo)
- **Alembic**: CURRENT (in application repo)
- **Gemini**: PLANNED (Application AI and analysis features have not yet been implemented)

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

### SAST (Static Application Security Testing) — PLANNED
All four SAST tools run in the Jenkins pipeline **before Docker build**. See [ADR-014](14-decisions/ADR-014-SAST.md) and [SAST Guide](10-security/SAST.md).
- **Bandit**: PLANNED — Python backend SAST (injection, crypto, hardcoded secrets)
- **npm audit**: PLANNED — React frontend dependency CVE scanning (native npm)
- **OWASP Dependency-Check**: PLANNED — Multi-ecosystem dependency scanning against NVD
- **Checkov**: PLANNED — Terraform IaC security misconfiguration scanning

### Image Security — PLANNED
- **Trivy**: PLANNED — Container image scanning (runs after Docker build)
- **Cosign**: PLANNED — Image signing and verification

### DAST (Dynamic Application Security Testing) — DEFERRED
- **OWASP ZAP**: DEFERRED — Requires stable test environment (Phase 7+). Tool selected, implementation deferred. See [SAST Guide](10-security/SAST.md) for reasoning.

## Configuration Management
- **Ansible**: PLANNED — manages ongoing mutable configuration of the Jenkins EC2 server (plugin setup, tool upgrades, service tuning, hardening). Complements Terraform (which provisions the instance) and Argo CD (which manages Kubernetes). See [ADR-013](14-decisions/ADR-013-Ansible.md).

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
- **Ansible as core K8s/app deployment mechanism**: HISTORICAL/REMOVED — Ansible was previously considered as a replacement for GitOps deployments. That use-case is removed. Ansible is now re-introduced specifically and only for EC2 configuration management.
- **Route 53 core requirement**: HISTORICAL/REMOVED
