# StockMind — Complete Project Master Handoff

**Document purpose:** This is the single source of context for the StockMind project. It is written so that a new developer, DevOps engineer, mentor, or another AI assistant can understand the project from the business idea through application architecture, cloud infrastructure, CI/CD, Kubernetes, observability, security, and future work.

**Repository:** https://github.com/shishir-krishna-101/StockMind.git  
**DevOps/Terraform repository:** `Stockmind-ops` (local path previously used: `D:\Stockmind-ops`)  
**Last consolidated:** September 2026

> **Important status rule:** This document distinguishes between **CURRENT**, **PLANNED**, **OPTIONAL**, and **HISTORICAL** information. Do not assume that a technology appearing in the architecture has already been deployed.

---

# 1. Executive Summary

StockMind is an inventory-management application designed to use AI to help businesses understand inventory demand, identify low-stock situations, forecast future demand, and provide useful inventory recommendations.

The project has two connected goals:

1. Build a useful full-stack application.
2. Build a realistic DevOps platform around it that demonstrates practical cloud, containerization, infrastructure-as-code, CI/CD, Kubernetes, security, and observability.

The intended production-style flow is broadly:

```text
Developer
   |
   v
GitHub
   |
   v
Jenkins CI
   |
   +--> Tests
   +--> SonarQube
   +--> Trivy
   +--> Docker build
   +--> Cosign signing
   |
   v
Amazon ECR
   |
   v
GitOps / Kubernetes manifests
   |
   v
Argo CD
   |
   v
Amazon EKS
   |
   +--> StockMind Frontend
   +--> StockMind Backend
   +--> AI-related workloads
   |
   +--> RDS PostgreSQL
   +--> Gemini API
   |
   +--> Observability
          +--> Prometheus
          +--> Grafana
          +--> Fluent Bit
          +--> Loki
          +--> OpenTelemetry
          +--> Tempo
          +--> Alertmanager
```

A later-stage intelligent operations concept is:

```text
Prometheus / Logs / Traces / Kubernetes events
                    |
                    v
             Alertmanager
                    |
                    v
          AI Incident Engine
                    |
                    v
            RCA + Recommendation
                    |
                    v
             Human Approval
                    |
                    v
          Controlled Remediation
          /        |        \
      restart     scale    rollback
```

The AI must **not** receive unrestricted cluster access. Remediation should be allowlisted and protected by validation and human approval.

---

# 2. Project Identity

## 2.1 Project name

**StockMind**

## 2.2 Application category

AI-assisted inventory-management / inventory intelligence application.

## 2.3 Main business problem

Businesses need to know:

- What inventory they currently have.
- Which products are becoming low in stock.
- What demand may look like in the future.
- Which products may face stockout risk.
- When they may need to reorder.
- What their inventory and sales data is telling them.

StockMind is intended to turn raw inventory/sales data into dashboards, alerts, forecasts, and recommendations.

## 2.4 DevOps objective

The DevOps implementation should demonstrate real operational concepts rather than being a collection of unrelated tools.

The project should demonstrate:

- Linux administration
- Docker
- Container image design
- AWS
- Terraform
- IAM
- VPC/networking
- ECR
- Jenkins
- CI security/scanning
- Kubernetes
- EKS
- GitOps
- Argo CD
- PostgreSQL/RDS
- Prometheus
- Grafana
- Loki
- Fluent Bit
- OpenTelemetry
- Tempo
- Alertmanager
- Controlled AI-assisted incident response

---

# 3. Current Application Architecture

## 3.1 Current application stack

The current application context is:

### Frontend
- React
- Frontend container/image

### Backend
- Python
- FastAPI
- SQLAlchemy
- Alembic
- JWT authentication
- PostgreSQL integration

### Database
- PostgreSQL

### AI
- Gemini API for AI functionality
- AI functionality is integrated into the application/backend
- A separate AI Incident Engine is planned for operational incident analysis

### Redis
**Removed from the current design because it was not being used.**

Do not re-add Redis merely because an older requirements document mentions it.

---

# 4. Application Components

## 4.1 Frontend

The frontend is the user-facing React application.

Responsibilities include:

- Login/authentication UI
- Inventory views
- Dashboard
- Product/inventory information
- Alerts
- Forecast information
- AI-related user functionality
- API calls to the backend

The frontend should not contain privileged infrastructure credentials.

## 4.2 Backend

The backend is a Python/FastAPI service.

Responsibilities include:

- API endpoints
- Authentication and authorization
- Business logic
- Inventory operations
- Database access
- JWT handling
- AI API integration
- Validation
- Error handling
- Database migrations through Alembic
- Structured logging

Conceptual flow:

```text
Frontend
   |
   | HTTP/API
   v
FastAPI Backend
   |
   +----> PostgreSQL
   |
   +----> Gemini API
```

## 4.3 PostgreSQL

PostgreSQL is the persistent relational database.

For the production-style AWS architecture, PostgreSQL is intended to run through **Amazon RDS** rather than as a normal application Pod.

The backend should be able to:

- Authenticate against the database.
- Read data.
- Write data.
- Execute required migrations.
- Maintain transactional inventory operations.

## 4.4 Gemini integration

The application can use Gemini for AI functionality.

The backend should communicate with Gemini rather than exposing the provider API key to the browser.

```text
User
 |
 v
Frontend
 |
 v
Backend
 |
 v
Gemini API
```

Secrets such as the Gemini API key must never be committed to Git.

---

# 5. Business AI vs AI Incident Engine

These two concepts must not be confused.

## 5.1 Application AI

Application AI helps the StockMind user.

Possible responsibilities:

- Demand prediction
- Stockout prediction
- Reorder recommendations
- Inventory analysis
- Business explanations
- Inventory assistant functionality

## 5.2 AI Incident Engine

The AI Incident Engine is a **DevOps/operations feature** planned for a later stage.

It analyzes production incidents using operational evidence.

Potential evidence:

- Prometheus metrics
- Application logs
- Distributed traces
- Kubernetes events
- Recent deployments
- Application health information

Example:

```text
Incident:
Backend error rate increased.

Evidence:
- HTTP 500 increased
- Database connection errors appear in logs
- A backend deployment occurred shortly before the incident

AI recommendation:
Rollback backend deployment.
```

The AI Incident Engine should recommend an action, not blindly execute arbitrary commands.

---

# 6. AI Safety Model

The AI operations architecture is intentionally constrained.

Unsafe model:

```text
Alert
  |
  v
AI
  |
  v
Unlimited kubectl access
```

Preferred model:

```text
Alert
  |
  v
AI Incident Engine
  |
  v
RCA + recommendation
  |
  v
Action validation
  |
  v
Human approval
  |
  v
Allowlisted remediation
```

Example allowed actions:

- restart
- scale
- rollback

Example:

```text
Backend CrashLoopBackOff
        |
        v
AI recommends restart
        |
        v
Human approves
        |
        v
Controller performs approved restart
```

The AI should not be allowed to:

- Delete arbitrary production resources.
- Execute arbitrary shell commands.
- Execute unrestricted SQL.
- Change permissions without authorization.
- Access secrets unnecessarily.
- Modify unrelated namespaces.
- Perform destructive actions without a controlled policy.

---

# 7. Repository Strategy

The project has been intentionally separated into application and infrastructure/operations repositories.

## 7.1 Application repository

**StockMind**

Repository:

```text
https://github.com/shishir-krishna-101/StockMind.git
```

This repository contains the application code.

Expected logical areas include:

```text
stockmind/
├── frontend/
├── backend/
├── ai-engine/        # if/when separated into its own service
├── tests/
├── database/
├── docs/
├── scripts/
├── .env.example
├── .gitignore
└── README.md
```

The exact tree may evolve with implementation.

## 7.2 DevOps repository

The DevOps/Terraform work is maintained separately.

Local path previously used:

```text
D:\Stockmind-ops
```

The operations repository was initialized as a Git repository.

The agreed high-level structure is:

```text
Stockmind-ops/
└── terraform/
    ├── ci/
    └── cd/
```

The CI side contains infrastructure such as:

- EC2
- ECR
- IAM

The CD side contains infrastructure/components such as:

- EKS
- networking
- RDS
- Argo CD-related deployment configuration
- secrets
- security groups
- providers
- variables
- outputs
- versions

---

# 8. Infrastructure Architecture

The project uses AWS as the main cloud platform.

The architecture is separated conceptually into:

```text
                    AWS
                     |
          +----------+----------+
          |                     |
        CI Layer              CD Layer
          |                     |
        EC2                  VPC / EKS
        Jenkins              RDS
        Trivy                ECR integration
        SonarQube            Kubernetes
        Docker               Argo CD
                              |
                           Observability
```

---

# 9. AWS Networking

## 9.1 VPC

A VPC provides the isolated network boundary for the infrastructure.

An example CIDR previously used while learning was:

```text
10.1.0.0/16
```

This is a **private RFC1918 network range** and is used as an example architecture value, not a claim that the production environment currently has exactly this CIDR.

## 9.2 Subnet

An example subnet was:

```text
10.1.1.0/24
```

A `/24` gives 256 total addresses, with AWS reserving some addresses.

Conceptually:

```text
VPC
10.1.0.0/16
      |
      +---- Subnet
            10.1.1.0/24
                  |
                  +---- EC2 private IP
```

If an EC2 instance receives a private IP such as:

```text
10.1.1.25
```

the next instance is not guaranteed to be `.26`; AWS allocates available addresses.

## 9.3 Public/private architecture

The production-style architecture should distinguish:

### Public-facing components
Potentially:

- Internet-facing load balancer
- NAT Gateway
- other intentionally public entry points

### Private components
Preferably:

- EKS worker/node networking
- RDS
- internal services
- databases

The goal is to avoid exposing databases directly to the Internet.

## 9.4 Internet Gateway

An Internet Gateway provides VPC connectivity to/from the public Internet for appropriately routed resources.

## 9.5 NAT Gateway

A NAT Gateway allows private subnet resources to make outbound Internet connections without making them directly Internet-addressable.

Typical reason:

```text
Private EC2/EKS workload
        |
        v
   NAT Gateway
        |
        v
    Internet
```

---

# 10. Security Groups

Security Groups act as stateful network firewalls around AWS resources.

Examples of intended communication:

```text
Internet
   |
   v
ALB
   |
   v
EKS application
   |
   v
RDS PostgreSQL
```

The RDS security group should allow PostgreSQL traffic only from the appropriate application/security group or network boundary.

Avoid using:

```text
0.0.0.0/0
```

for sensitive internal services unless there is a specific documented reason.

---

# 11. IAM

IAM controls AWS permissions.

The project should use IAM roles rather than embedding AWS access keys inside:

- Docker images
- source code
- Git repositories
- Kubernetes manifests

Important principle:

```text
Workload
   |
   v
IAM Role
   |
   v
Specific AWS permissions
```

Permissions should follow least privilege.

The Terraform CI/CD infrastructure includes IAM-related resources/configuration.

---

# 12. EC2 CI Server

The CI layer uses an EC2 instance as the Jenkins/build server.

The conceptual setup is:

```text
AWS VPC
 |
 +---- CI subnet
        |
        +---- EC2
              |
              +---- Jenkins
              +---- Docker
              +---- Trivy
              +---- SonarQube
              +---- Java
```

Earlier project discussions considered a dedicated storage volume for the CI server, including a 30 GB gp3 example.

Exact instance type, volume size, AMI, and public IP should always be taken from the current Terraform variables/state rather than assumed from this document.

---

# 13. ECR

Amazon Elastic Container Registry is the image registry.

The application uses separate images for separate components.

Conceptually:

```text
ECR
 |
 +-- stockmind-frontend
 |
 +-- stockmind-backend
 |
 +-- stockmind-ai-incident-engine
```

If a component is not actually separated into its own deployable service yet, do not create an unnecessary repository just for the sake of having more repositories.

The repository count should match actual independently deployed container components.

---

# 14. Docker Architecture

Each independently deployed component can have its own Dockerfile.

The earlier design discussion was:

```text
frontend/
  Dockerfile

backend/
  Dockerfile

ai-engine/
  Dockerfile
```

The general concept is:

```text
Source code
   |
   v
Dockerfile
   |
   v
Docker image
   |
   v
ECR
   |
   v
EKS
```

## 14.1 Dockerfile principles

Use:

- appropriate base images
- `.dockerignore`
- multi-stage builds where useful
- non-root users where practical
- small runtime images
- deterministic dependency installation
- no secrets baked into images

## 14.2 Build vs runtime

Build-time dependencies should not unnecessarily remain in the final runtime image.

For example:

```text
Builder image
    |
    | build
    v
Application artifacts
    |
    v
Small runtime image
```

---

# 15. CI Pipeline

Jenkins is the planned CI orchestration tool.

A production-style pipeline is:

```text
Developer
   |
   v
GitHub
   |
   v
Jenkins
   |
   +--> Checkout
   |
   +--> Test
   |
   +--> Static analysis
   |       |
   |       +--> SonarQube
   |
   +--> Dependency/image scanning
   |       |
   |       +--> Trivy
   |
   +--> Docker build
   |
   +--> Image scan
   |
   +--> Image signing
   |       |
   |       +--> Cosign
   |
   +--> Push image
           |
           v
          ECR
```

The exact Jenkinsfile stages should match what is actually implemented.

---

# 16. SonarQube

SonarQube is intended for code-quality/static analysis.

Typical CI role:

```text
Source
  |
  v
SonarQube analysis
  |
  v
Quality findings / quality gate
```

It is not a container runtime security scanner.

---

# 17. Trivy

Trivy is used as a security scanner.

It can be used in CI to scan:

- container images
- filesystem/dependencies
- configuration/IaC in appropriate workflows

Typical flow:

```text
Docker build
    |
    v
Trivy scan
    |
    +---- pass --> continue
    |
    +---- fail --> stop/fix
```

The exact failure thresholds should be explicitly configured rather than assumed.

---

# 18. Cosign

Cosign is intended for container image signing.

Conceptually:

```text
Build image
    |
    v
Scan image
    |
    v
Sign image
    |
    v
Push/use signed artifact
```

The production implementation should use secure key management rather than committing signing secrets to Git.

---

# 19. CD / GitOps

The CD side is intended to use Argo CD.

The conceptual model:

```text
Git repository
     |
     | desired state
     v
  Argo CD
     |
     v
   EKS
     |
     v
Kubernetes resources
```

Argo CD continuously reconciles the desired state in Git with the Kubernetes cluster.

This separates:

- **CI:** build/test/scan/package
- **CD:** deploy/reconcile

---

# 20. EKS

Amazon EKS is the planned production Kubernetes platform.

The cluster should run application workloads such as:

```text
EKS
 |
 +-- Frontend Deployment
 |     +-- frontend Pods
 |
 +-- Backend Deployment
 |     +-- backend Pods
 |
 +-- AI Incident Engine Deployment
       +-- AI Pods
```

Kubernetes Services provide stable internal networking.

---

# 21. Kubernetes Application Networking

Conceptually:

```text
Internet
   |
   v
AWS ALB
   |
   v
Ingress
   |
   v
Frontend Service
   |
   v
Frontend Pods
   |
   v
Backend Service
   |
   v
Backend Pods
   |
   +----> RDS PostgreSQL
   |
   +----> Gemini API
```

The frontend should generally communicate with the backend through a controlled API path rather than exposing database access to the frontend.

---

# 22. AWS Load Balancer Controller

The AWS Load Balancer Controller is the bridge between Kubernetes resources and AWS load balancers.

For example:

```text
Kubernetes Ingress
       |
       v
AWS Load Balancer Controller
       |
       v
AWS Application Load Balancer
```

This enables an Internet-facing flow such as:

```text
User
 |
 v
ALB
 |
 v
Ingress
 |
 v
Frontend Service
 |
 v
Frontend Pods
```

This is different from Istio.

---

# 23. Istio

Istio is part of the planned service-mesh layer.

It is intended for internal service-to-service traffic and can provide:

- mTLS
- traffic management
- retries
- timeouts
- traffic splitting
- telemetry
- service-to-service security

Conceptually:

```text
Frontend
   |
   v
Istio
   |
   v
Backend
   |
   v
Istio
   |
   v
AI Engine
```

Istio should not be installed simply because it appears on a technology list. It should be introduced when the service-to-service requirements justify it.

---

# 24. Application Deployment Verification

A successful Kubernetes deployment is not just:

```text
kubectl get pods
```

showing `Running`.

The complete application path must be tested.

## Test 1 — Internet to frontend

```text
Internet
  |
  v
ALB
  |
  v
Frontend
```

Verify that the application loads.

## Test 2 — Frontend to backend

```text
Frontend
  |
  v
API endpoint
  |
  v
Backend
```

Verify authentication and API calls.

## Test 3 — Backend to RDS

Verify that the backend can:

- connect
- authenticate
- read
- write
- execute required migrations

## Test 4 — Backend to Gemini

```text
Backend
   |
   v
Gemini API
```

Verify the AI functionality.

The complete chain is:

```text
User
 |
 v
ALB
 |
 v
Frontend
 |
 v
Backend
 |       \
 |        \
 v         v
RDS      Gemini
```

---

# 25. Observability Architecture

The project intentionally separates the three major observability signals:

```text
Metrics  -> Prometheus
Logs     -> Fluent Bit -> Loki
Traces   -> OpenTelemetry -> Tempo
```

Grafana provides the visualization layer.

Combined:

```text
                 Grafana
              /     |      \
             /      |       \
            v       v        v
      Prometheus   Loki     Tempo
         ^           ^        ^
         |           |        |
      Metrics    Fluent Bit  OTel
```

---

# 26. Prometheus

Prometheus is the metrics system.

Typical metrics include:

- CPU usage
- Memory usage
- Request count
- Request latency
- HTTP error rate
- Pod restarts
- Kubernetes health metrics

Example:

```text
backend_cpu_usage = 72%
http_requests_total = 15234
```

Prometheus stores time-series metrics.

---

# 27. Grafana

Grafana is the visualization layer.

It can connect to:

- Prometheus
- Loki
- Tempo

A unified dashboard can show:

```text
Metrics + Logs + Traces
```

This is useful for troubleshooting.

For example:

```text
High latency
   |
   v
Prometheus shows latency spike
   |
   v
Grafana links to relevant logs
   |
   v
Loki shows database errors
   |
   v
Tempo shows slow database/Gemini span
```

---

# 28. Loki

Loki is the log aggregation backend.

Application examples:

```text
INFO user logged in
INFO inventory updated
ERROR database connection failed
```

Instead of manually running:

```text
kubectl logs ...
```

for every Pod, logs can be centralized.

Conceptually:

```text
Pods
 |
 v
Loki
 |
 v
Grafana
```

Loki stores/serves logs and metadata for querying.

---

# 29. Fluent Bit

Fluent Bit is the log collector/forwarder.

Typical architecture:

```text
Kubernetes Nodes
 |
 +-- application logs
 |
 v
Fluent Bit
 |
 v
Loki
 |
 v
Grafana
```

Fluent Bit is commonly deployed as a Kubernetes DaemonSet.

A DaemonSet generally places one Fluent Bit Pod on each node.

Example:

```text
Node 1
 +-- Frontend Pod
 +-- Backend Pod
 +-- Fluent Bit

Node 2
 +-- Backend Pod
 +-- AI Pod
 +-- Fluent Bit
```

Key distinction:

**Fluent Bit collects/forwards logs. Loki stores/serves them. Grafana visualizes them.**

---

# 30. OpenTelemetry

OpenTelemetry is used for telemetry collection/instrumentation, especially distributed tracing in this architecture.

Example request:

```text
Frontend
   |
   v
Backend
   |
   v
PostgreSQL
   |
   v
Gemini
```

Suppose the complete request takes 4 seconds.

Tracing can help identify where the time went:

```text
Frontend     50ms
Backend     100ms
RDS         150ms
Gemini     3700ms
```

OpenTelemetry can propagate trace context and send trace data toward the trace backend.

---

# 31. Tempo

Tempo is the planned trace backend.

The mental model:

```text
Metrics
   |
Prometheus

Logs
   |
Fluent Bit
   |
Loki

Traces
   |
OpenTelemetry
   |
Tempo
```

Grafana can visualize all three.

---

# 32. Alertmanager

Prometheus can evaluate alert rules.

Example:

```text
Backend error rate > 5%
```

The alert can flow to Alertmanager.

```text
Prometheus
   |
   v
Alert rule triggered
   |
   v
Alertmanager
   |
   v
Notification / webhook
```

For the advanced StockMind design:

```text
Prometheus
   |
   v
Alertmanager
   |
   v
AI Incident Engine
```

---

# 33. AI Incident Response Flow

The advanced operations flow is:

```text
Application / Kubernetes
        |
        +---- Metrics
        +---- Logs
        +---- Traces
        +---- Events
        |
        v
Observability Stack
        |
        v
Prometheus / Alertmanager
        |
        v
AI Incident Engine
        |
        +---- gather evidence
        +---- correlate signals
        +---- inspect recent deployment
        +---- generate RCA
        |
        v
Recommendation
        |
        v
Human Approval
        |
        v
Action Validation
        |
        v
Controlled Remediation
```

Example incident:

```text
Backend CrashLoopBackOff
```

Possible evidence:

```text
- Pod restarts increased
- HTTP 500 increased
- Logs contain database connection errors
- A backend release occurred recently
```

Possible recommendation:

```text
Rollback backend deployment
```

Human approves.

The remediation controller performs the allowlisted action.

---

# 34. Controlled Remediation

The remediation system should use an allowlist.

Example:

```text
Allowed:
- restart
- scale
- rollback
```

Conceptual validation:

```text
AI Recommendation
       |
       v
Action Validator
       |
       v
Is action allowlisted?
    /          \
  Yes           No
   |             |
   v             v
Approval       Reject
   |
   v
Execute
```

The controller should also verify:

- target namespace
- target workload
- action type
- authorization
- current state
- safety policy

---

# 35. AWS Services Considered

The project has discussed a broad AWS ecosystem.

Core/currently relevant:

- EC2
- VPC
- Public/private subnets
- Internet Gateway
- NAT Gateway
- Security Groups
- IAM
- ECR
- EKS
- RDS

Other services have been discussed for security/production hardening:

- S3
- EFS
- CloudWatch
- WAF
- Shield
- GuardDuty
- Security Hub
- CloudFront
- Route 53

These are **not all mandatory components** of the first implementation.

The architecture should avoid adding services only to make the project look larger.

---

# 36. Terraform Design

Terraform is the Infrastructure-as-Code layer.

The repository is divided into:

```text
terraform/
├── ci/
└── cd/
```

## CI Terraform

Expected responsibilities:

- AWS provider
- CI EC2
- security groups
- IAM
- ECR
- variables
- outputs
- versions

## CD Terraform

Expected responsibilities:

- VPC/networking
- EKS
- managed node groups
- RDS
- security groups
- secrets-related infrastructure
- variables
- outputs
- versions

Argo CD application manifests/configuration belong conceptually to the Kubernetes/CD layer rather than being confused with basic AWS infrastructure creation.

---

# 37. Terraform Mental Model

A simplified Terraform flow:

```text
main.tf
variables.tf
outputs.tf
versions.tf
provider/config
      |
      v
terraform init
      |
      v
terraform plan
      |
      v
terraform apply
      |
      v
AWS resources
```

Important commands:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform destroy
terraform output
terraform state list
terraform show
```

The exact commands used depend on the working directory and backend/state configuration.

---

# 38. Terraform File Roles

## main.tf

Contains resource/module/provider configuration as appropriate.

## variables.tf

Defines configurable inputs.

Example:

```hcl
variable "instance_type" {
  type = string
}
```

## outputs.tf

Exposes useful resulting values.

Example:

```hcl
output "vpc_id" {
  value = aws_vpc.main.id
}
```

## versions.tf

Defines Terraform/provider version constraints.

## terraform.tfvars

Contains environment-specific values when used.

Secrets should not be casually stored in plain text tfvars files committed to Git.

---

# 39. Environment Separation

The architecture should keep environment-specific values configurable.

Potential environments:

```text
dev
staging
prod
```

Do not hard-code:

- public IP addresses
- passwords
- API keys
- private keys
- database secrets

into source code.

---

# 40. Secrets Management

Development:

```text
.env
```

may be used locally.

But:

```text
.env
```

must not be committed if it contains secrets.

Production should use an appropriate secret-management mechanism.

Potential secrets include:

- PostgreSQL username/password
- Gemini API key
- SMTP credentials
- other third-party API credentials

Secrets must not appear in:

- Git
- Docker images
- public logs
- frontend bundles
- error messages

---

# 41. Database Architecture

Production-style:

```text
EKS Backend Pods
       |
       v
RDS PostgreSQL
```

The database should be placed behind appropriate security groups/private networking.

Application migrations can be handled through the backend's Alembic workflow, with a controlled deployment process.

Critical inventory changes should be transactional.

Example:

```text
Create Order
+
Reserve/Reduce Inventory
```

must not partially succeed.

---

# 42. Backup and Disaster Recovery

Production database planning should include:

- Automated backups
- Backup retention
- Point-in-time recovery where supported
- Restore testing
- Disaster-recovery procedure

Document:

- RPO
- RTO
- backup strategy
- restore procedure

Do not claim disaster recovery is implemented until restore testing has actually been performed.

---

# 43. Scalability Principles

The application should be able to grow without immediately introducing unnecessary complexity.

Useful principles:

- Stateless API design
- Database connection pooling
- Efficient queries
- Proper database indexes
- Pagination
- Background jobs for expensive tasks
- Horizontal application scaling
- Controlled caching when actually needed

Redis was previously considered but was removed because it was not used.

---

# 44. Kubernetes Reliability

Relevant Kubernetes features for the project include:

- Deployments
- ReplicaSets
- StatefulSets where appropriate
- Services
- Ingress
- Readiness probes
- Liveness probes
- Startup probes
- Resource requests
- Resource limits
- HPA
- VPA where justified
- NetworkPolicy
- RBAC
- Pod disruption considerations

Not every feature needs to be implemented immediately.

---

# 45. Kubernetes Core Concepts for This Project

## API Server

Central API interface for Kubernetes.

## etcd

Stores cluster state.

## Scheduler

Chooses nodes for Pods.

## Controller Manager

Runs controllers that reconcile desired and actual state.

## kubelet

Runs on nodes and manages Pods/containers.

## CNI

Provides Pod networking.

Calico was used/considered during earlier kubeadm learning and troubleshooting.

The project production architecture uses EKS rather than requiring a manually maintained kubeadm cluster.

---

# 46. Earlier Kubernetes Learning Issues

During the user's hands-on Kubernetes learning, a kubeadm cluster experienced:

- `NotReady` nodes
- Calico `Init:CrashLoopBackOff`
- CoreDNS Pending
- Calico permission issues writing to host CNI directories
- manifest/version compatibility issues

These were learning/troubleshooting experiences and should not be confused with the intended production EKS architecture.

---

# 47. Current Tool Decisions

The following decisions were made during project development:

### Redis
**Removed** because it was unused.

### Karpenter
**Removed** from the project design.

### Ansible
Earlier architecture discussions included Ansible for CI-server configuration. The later agreed operations structure is centered on Terraform CI/CD and does not rely on Ansible as a core project component.

### Route 53
Earlier discussions considered it, but it was later removed from the planned core stack.

### Loki
Added to the observability architecture for centralized logs.

### OpenTelemetry
Used as the telemetry/tracing layer and complements Prometheus rather than replacing it.

### Prometheus
Metrics.

### Grafana
Visualization.

### Fluent Bit
Log collection/forwarding.

### Loki
Log backend.

### Tempo
Trace backend.

### Istio
Planned service mesh layer, not something that must be installed before the basic application works.

---

# 48. Why OpenTelemetry and Prometheus Both Exist

They solve different problems.

Prometheus:

```text
Metrics
CPU
Memory
Request count
Error rate
```

OpenTelemetry:

```text
Telemetry instrumentation/collection
especially distributed traces
```

A useful architecture is:

```text
Metrics
   |
Prometheus

Traces
   |
OpenTelemetry
   |
Tempo
```

They are complementary.

---

# 49. Why Fluent Bit and Loki Both Exist

They are not duplicates.

Fluent Bit:

```text
Collect + transform + forward logs
```

Loki:

```text
Store/serve/query logs
```

Grafana:

```text
Visualize logs
```

So:

```text
Pod logs
   |
   v
Fluent Bit
   |
   v
Loki
   |
   v
Grafana
```

---

# 50. Complete End-to-End Architecture

The complete conceptual architecture is:

```text
                         INTERNET
                             |
                             v
                       AWS ALB
                             |
                             v
                 AWS Load Balancer Controller
                             |
                             v
                         INGRESS
                             |
                             v
                    FRONTEND SERVICE
                             |
                             v
                    FRONTEND PODS
                             |
                             v
                    BACKEND SERVICE
                             |
                             v
                    BACKEND PODS
                       /           \
                      /             \
                     v               v
             RDS POSTGRESQL     GEMINI API

                 Internal service traffic
                         |
                         v
                        ISTIO

                 OBSERVABILITY LAYER
             /          |             \
            /           |              \
       METRICS         LOGS           TRACES
          |              |               |
          v              v               v
     Prometheus      Fluent Bit     OpenTelemetry
                         |               |
                         v               v
                        Loki            Tempo
            \              |             /
             \             |            /
              +------------v-----------+
                           |
                        Grafana
                           |
                           v
                      Visibility
                           |
                           v
                     Alertmanager
                           |
                           v
                  AI Incident Engine
                           |
                           v
                  RCA + Recommendation
                           |
                           v
                    Human Approval
                           |
                           v
                 Action Validation
                           |
                           v
                Controlled Remediation
                 /        |        \
             restart     scale     rollback
```

---

# 51. CI/CD End-to-End Architecture

```text
                 DEVELOPER
                     |
                     v
                  GITHUB
                     |
                     v
                  JENKINS
                     |
       +-------------+-------------+
       |             |             |
      Test       SonarQube       Trivy
       |             |             |
       +-------------+-------------+
                     |
                     v
                Docker Build
                     |
                     v
                 Trivy Scan
                     |
                     v
                  Cosign
                     |
                     v
                   ECR
                     |
                     v
             GitOps Manifest
                     |
                     v
                 ARGO CD
                     |
                     v
                   EKS
                     |
         +-----------+-----------+
         |           |           |
      Frontend    Backend    AI Engine
         |           |           |
         +-----------+-----------+
                     |
                     v
                 PostgreSQL
```

---

# 52. What Happens During a Deployment

A normal application release should conceptually work like this:

1. Developer changes code.
2. Developer pushes to GitHub.
3. Jenkins detects the change.
4. Jenkins checks out source.
5. Tests run.
6. SonarQube analyzes code.
7. Trivy scans dependencies/configuration/images as configured.
8. Docker images are built.
9. Images are tagged.
10. Images are signed with Cosign where configured.
11. Images are pushed to ECR.
12. Kubernetes desired state is updated through the GitOps workflow.
13. Argo CD detects the desired-state change.
14. Argo CD reconciles EKS.
15. Kubernetes performs the deployment.
16. Readiness/liveness/startup checks validate workloads.
17. Application smoke tests verify the end-to-end path.
18. Prometheus/Grafana/Loki/Tempo provide operational visibility.

---

# 53. Rollout Verification

Do not consider a release successful merely because an image was pushed.

Verify:

```text
Image exists
   |
   v
Kubernetes rollout successful
   |
   v
Pods Ready
   |
   v
Service reachable
   |
   v
Frontend works
   |
   v
Backend API works
   |
   v
RDS works
   |
   v
Gemini functionality works
   |
   v
Logs/metrics/traces visible
```

---

# 54. Failure Scenarios the Project Should Demonstrate

The project can be used to demonstrate practical incident handling.

## Scenario A — Backend CrashLoopBackOff

Symptoms:

```text
Pod restarting
```

Investigation:

```text
kubectl get pods
kubectl describe pod
kubectl logs
Grafana
Loki
```

Possible root cause:

- invalid environment variable
- application startup failure
- database connection problem

## Scenario B — High HTTP error rate

Prometheus detects:

```text
HTTP 500 > threshold
```

Then:

```text
Alertmanager
   |
   v
AI Incident Engine
```

The engine correlates:

- metrics
- logs
- deployment history

and recommends a controlled action.

## Scenario C — Database connectivity failure

Flow:

```text
Backend
   |
   X
RDS
```

Check:

- security groups
- route/networking
- DNS
- credentials
- database availability
- connection pool
- application logs

## Scenario D — Bad release

A new backend version causes errors.

Possible controlled remediation:

```text
Bad release
   |
   v
Detect
   |
   v
Analyze
   |
   v
Recommend rollback
   |
   v
Human approval
   |
   v
Rollback
```

---

# 55. Security Architecture

Security should exist at multiple layers.

## Source control

- No secrets committed.
- Branch/protection policies where appropriate.
- Review important changes.

## CI

- Dependency scanning.
- Image scanning.
- Static analysis.
- Artifact signing.

## Docker

- Small images.
- Non-root runtime where practical.
- No secrets in images.

## AWS

- IAM least privilege.
- Security groups.
- Private database networking.
- Encryption where appropriate.

## Kubernetes

- RBAC.
- NetworkPolicy where appropriate.
- Secrets management.
- Resource limits.
- Pod security controls.

## Application

- JWT authentication.
- Authorization.
- Input validation.
- Secure password handling.
- Safe error messages.

---

# 56. Observability Troubleshooting Method

When an incident happens, use a structured process.

## Step 1 — Metrics

Ask:

- Did traffic increase?
- Did error rate increase?
- Did latency increase?
- Did CPU/memory change?
- Did Pods restart?

Use Prometheus/Grafana.

## Step 2 — Logs

Ask:

- What errors appeared?
- When did they begin?
- Which component produced them?

Use Loki/Grafana.

## Step 3 — Traces

Ask:

- Which service is slow?
- Is database access slow?
- Is Gemini slow?
- Is an internal API call failing?

Use OpenTelemetry/Tempo/Grafana.

## Step 4 — Kubernetes

Check:

```text
Pods
Deployments
Services
Events
Ingress
resources
probes
```

## Step 5 — Recent changes

Ask:

```text
What changed immediately before the incident?
```

This can include:

- application release
- configuration
- infrastructure
- database migration
- dependency

---

# 57. Project Status Model

Because this document is intended for other people and AIs, status must be explicit.

## CURRENT / CONFIRMED CONTEXT

- StockMind application exists as the main project.
- Application uses React frontend.
- Backend uses FastAPI/Python.
- PostgreSQL is the database.
- JWT authentication is part of the backend.
- SQLAlchemy/Alembic are part of the backend stack.
- Gemini is part of the AI application functionality.
- Redis was removed because it was unused.
- Application and DevOps work are separated into repositories.
- `Stockmind-ops` contains Terraform CI/CD structure.
- CI/CD infrastructure planning includes EC2/ECR/IAM on CI and EKS/RDS/networking/CD components.
- Observability architecture uses Prometheus/Grafana/Loki/Fluent Bit/OpenTelemetry/Tempo/Alertmanager conceptually.

## PLANNED

- Full production-style EKS deployment.
- Argo CD GitOps deployment.
- AWS Load Balancer Controller.
- Advanced observability integration.
- Istio service mesh.
- AI Incident Engine.
- Human-approved controlled remediation.

## OPTIONAL / LATER

- Additional AWS security services such as WAF, GuardDuty, Security Hub.
- CloudFront.
- S3/EFS where a concrete application requirement exists.
- Advanced autoscaling components.

## HISTORICAL / DO NOT ASSUME CURRENT

- Redis in the application stack.
- Ansible as a core current deployment mechanism.
- Karpenter as a core component.
- Route 53 as a required core component.
- Manual kubeadm/Calico cluster as the production platform.

---

# 58. Important Rule for Future AI Assistants

If another AI receives this document, it must not assume:

> "Everything mentioned here is already implemented."

Instead use:

```text
CURRENT = confirmed project context
PLANNED = architecture/design to implement
OPTIONAL = possible later enhancement
HISTORICAL = previous approach/learning experience
```

When giving implementation instructions, the AI should first identify which status applies to the component.

---

# 59. How Another Developer Should Start

A new developer should understand the project in this order:

## Phase 1 — Understand the application

Read:

```text
frontend
backend
database configuration
AI/Gemini integration
README
.env.example
```

Understand:

```text
Frontend -> Backend -> PostgreSQL
                    |
                    -> Gemini
```

## Phase 2 — Run locally

Get the application working locally before touching EKS.

Verify:

- frontend starts
- backend starts
- database connection works
- authentication works
- core inventory functions work
- AI functionality works

## Phase 3 — Containerize

Build:

```text
frontend image
backend image
AI image if separately deployed
```

Run locally with Docker and verify networking.

## Phase 4 — AWS infrastructure

Implement/verify:

```text
VPC
subnets
security groups
IAM
ECR
CI EC2
EKS
RDS
```

## Phase 5 — CI

Implement Jenkins:

```text
checkout
test
quality
security scan
build
sign
push
```

## Phase 6 — CD

Implement:

```text
GitOps
Argo CD
EKS deployments
services
ingress
```

## Phase 7 — Application verification

Verify:

```text
ALB -> frontend -> backend -> RDS/Gemini
```

## Phase 8 — Observability

Add:

```text
Prometheus
Grafana
Fluent Bit
Loki
OpenTelemetry
Tempo
Alertmanager
```

## Phase 9 — Advanced operations

Only after the basics work:

```text
Istio
AI Incident Engine
Human Approval
Controlled Remediation
```

---

# 60. Definition of Done

A feature should not be considered complete merely because its code exists.

A reasonable definition of done is:

- Code implemented.
- Validation implemented.
- Error handling implemented.
- Tests added where appropriate.
- Authorization checked.
- API documented.
- Database migration updated where required.
- Logging implemented.
- UI loading/error states implemented where relevant.
- Deployment configuration updated.
- Documentation updated.
- Security implications reviewed.
- Operational verification completed.

For infrastructure:

- Terraform validates.
- Terraform plan reviewed.
- Resources created successfully.
- Connectivity tested.
- Security groups reviewed.
- IAM permissions reviewed.
- Outputs recorded.
- Destruction/recovery implications understood.

For Kubernetes:

- Manifests validate.
- Pods become Ready.
- Probes work.
- Services work.
- Ingress works.
- Application dependencies work.
- Logs are visible.
- Metrics are visible.
- Rollout/rollback behavior is understood.

---

# 61. Useful Interview Explanation

If asked "Explain your StockMind project", the concise architecture explanation is:

> StockMind is an inventory-management application with AI-assisted demand prediction and low-stock intelligence. The application uses a React frontend, FastAPI/Python backend, PostgreSQL, JWT authentication, SQLAlchemy/Alembic, and Gemini for AI functionality. I separated the application and infrastructure repositories. For the DevOps side, I use Terraform to provision AWS infrastructure, Docker for containerization, ECR for image storage, Jenkins for CI, Trivy/SonarQube/Cosign for security and quality, EKS for Kubernetes deployment, and Argo CD for GitOps-based CD. For observability, the architecture uses Prometheus and Grafana for metrics, Fluent Bit and Loki for logs, and OpenTelemetry and Tempo for traces. A later-stage AI Incident Engine can correlate operational signals and recommend controlled remediation, but actions are gated by validation and human approval.

---

# 62. Common Questions a New AI Should Ask Before Changing the Project

Before making a major implementation change, check:

1. Is the component already implemented or only planned?
2. Is this an application change or DevOps change?
3. Does the change belong in the StockMind repo or Stockmind-ops repo?
4. Does it introduce a new AWS service?
5. Does it introduce a new container?
6. Does it require a new ECR repository?
7. Does it require new IAM permissions?
8. Does it expose a new network path?
9. Does it introduce a new secret?
10. Does it change the Kubernetes deployment model?
11. Does it affect the CI pipeline?
12. Does it affect the GitOps/CD flow?
13. How will the change be monitored?
14. How will the change be rolled back?
15. Is there a simpler solution that satisfies the same requirement?

---

# 63. Repository/Architecture Relationship

The clean mental model is:

```text
                 TWO MAIN REPOSITORIES

       StockMind                    Stockmind-ops
           |                              |
           v                              v
    Application code             Infrastructure/IaC
           |                              |
    +------+------+                 +-----+------+
    |      |      |                 |            |
Frontend Backend AI              Terraform    Kubernetes/CD
    |      |      |                 |            |
    +------+------+                 +-----+------+
           |                              |
           v                              v
       Docker images                    AWS/EKS
           |                              |
           +------------+-----------------+
                        |
                        v
                    Production
```

---

# 64. Practical Rules for Continuing the Project

1. Keep application and infrastructure concerns separated.
2. Do not add tools merely to increase the technology count.
3. Prefer the simplest architecture that demonstrates the concept clearly.
4. Do not claim a component is deployed until it has been tested.
5. Keep secrets outside Git.
6. Use least-privilege IAM.
7. Keep databases private.
8. Scan images before deployment.
9. Use immutable/versioned image tags rather than relying only on `latest`.
10. Make Kubernetes deployments observable.
11. Test rollback.
12. Document every significant architecture decision.
13. Keep planned and implemented components clearly separated.
14. For AI operations, require validation and human approval for meaningful production actions.

---

# 65. Final Mental Model

The entire project can be remembered as five layers.

## Layer 1 — Product

```text
StockMind
Frontend
Backend
PostgreSQL
Gemini
```

## Layer 2 — Containers

```text
Docker
Images
ECR
```

## Layer 3 — Infrastructure

```text
Terraform
AWS
VPC
IAM
EC2
EKS
RDS
```

## Layer 4 — Delivery

```text
GitHub
Jenkins
SonarQube
Trivy
Cosign
Argo CD
```

## Layer 5 — Operations

```text
Prometheus
Grafana
Fluent Bit
Loki
OpenTelemetry
Tempo
Alertmanager
AI Incident Engine
Human Approval
Controlled Remediation
```

The intended overall lifecycle is:

```text
CODE
  |
  v
BUILD
  |
  v
TEST
  |
  v
SCAN
  |
  v
SIGN
  |
  v
PUSH TO ECR
  |
  v
GITOPS
  |
  v
ARGO CD
  |
  v
EKS
  |
  v
STOCKMIND
  |
  v
OBSERVE
  |
  v
DETECT
  |
  v
ANALYZE
  |
  v
HUMAN APPROVAL
  |
  v
CONTROLLED REMEDIATION
```

---

# 66. AI Handoff Prompt

The following prompt can be given together with this document to another AI:

> You are now working as the technical assistant for the StockMind project.
>
> Treat this document as the primary project context.
>
> StockMind is an inventory-management application with AI-assisted demand prediction and low-stock intelligence. The current application uses React, FastAPI/Python, PostgreSQL, JWT authentication, SQLAlchemy/Alembic, and Gemini. Redis was removed because it was unused.
>
> The application repository and DevOps/Terraform repository are separated. The DevOps repository is `Stockmind-ops` and contains `terraform/ci` and `terraform/cd`.
>
> The intended DevOps architecture uses AWS, Terraform, Docker, ECR, Jenkins, SonarQube, Trivy, Cosign, EKS, Argo CD, Prometheus, Grafana, Fluent Bit, Loki, OpenTelemetry, Tempo, and Alertmanager. Istio and an AI Incident Engine are advanced/planned components. The AI Incident Engine must not have unrestricted Kubernetes access; important remediation actions require validation and human approval.
>
> Important: do not assume that every component described in the architecture is already implemented. Use the status sections in this document. If implementation status is unclear, inspect the current repository/files or ask for the relevant current configuration rather than inventing it.
>
> When suggesting changes:
> 1. Explain where the change belongs: StockMind repo or Stockmind-ops repo.
> 2. Explain dependencies.
> 3. Explain AWS/IAM/network/security implications.
> 4. Provide implementation steps in the correct order.
> 5. Give verification commands/tests.
> 6. Explain rollback/recovery where relevant.
> 7. Do not introduce additional tools unless they solve a real requirement.
> 8. Never put secrets directly into code, Terraform, Dockerfiles, Kubernetes manifests, or Git.
>
> Prefer practical, beginner-friendly explanations because the project owner is learning DevOps. Do not assume expert-level knowledge simply because a tool appears in the architecture.
