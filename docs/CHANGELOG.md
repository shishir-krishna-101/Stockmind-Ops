# Roadmap and Changelog

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
