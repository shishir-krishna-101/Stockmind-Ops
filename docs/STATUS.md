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
