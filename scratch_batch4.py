from scratch_gen_docs_helper import write_doc, adr_template

adr1 = adr_template("001", "Terraform for Infrastructure as Code", "Accepted", 
    "Need a reproducible way to provision cloud infrastructure.", 
    "Use Terraform as the primary IaC tool.", 
    "CloudFormation, Pulumi, AWS CDK", 
    "Terraform has broad adoption, excellent documentation, and works across providers.", 
    "Requires learning HCL and managing state files.", 
    "All infrastructure changes must go through code.", 
    "Reconsider if the team strongly prefers writing infrastructure in a general-purpose programming language (Pulumi/CDK).")

adr2 = adr_template("002", "AWS as Cloud Provider", "Accepted", 
    "Need a public cloud provider for the project.", 
    "Use AWS.", 
    "GCP, Azure", 
    "Familiarity with the ecosystem and availability of strong managed services like EKS and RDS.", 
    "Vendor lock-in to AWS specific services.", 
    "The architecture is AWS-centric.", 
    "Reconsider if costs become prohibitive or multi-cloud is mandated.")

adr3 = adr_template("003", "EKS for Kubernetes", "Accepted", 
    "Need a container orchestration platform.", 
    "Use Amazon EKS.", 
    "Self-managed Kubernetes, ECS", 
    "Reduces the operational burden of managing the control plane while maintaining K8s compatibility.", 
    "EKS control plane has a flat hourly fee.", 
    "Kubernetes becomes the deployment target for all workloads.", 
    "Reconsider if Kubernetes operational complexity outweighs benefits.")

adr4 = adr_template("004", "RDS PostgreSQL", "Accepted", 
    "Need a reliable relational database for the application.", 
    "Use managed Amazon RDS PostgreSQL.", 
    "Self-hosted PostgreSQL in K8s, Aurora", 
    "RDS handles backups, patching, and high availability without K8s statefulset complexity. PostgreSQL was chosen over MySQL for JSON support and advanced features.", 
    "Higher cost than self-hosting.", 
    "Database state is externalized from the Kubernetes cluster.", 
    "Reconsider if database costs are too high, requiring self-hosting.")

adr5 = adr_template("005", "ECR for Container Registry", "Accepted", 
    "Need to store Docker images securely.", 
    "Use Amazon ECR.", 
    "Docker Hub, GHCR", 
    "Deep IAM integration with EKS and EC2 Jenkins host.", 
    "Vendor lock-in.", 
    "Images are stored securely within the AWS boundary.", 
    "Reconsider if migrating away from AWS.")

adr6 = adr_template("006", "Jenkins for CI", "Accepted", 
    "Need a CI server for building and scanning images.", 
    "Use Jenkins on a dedicated EC2 instance.", 
    "GitHub Actions, GitLab CI", 
    "Provides full control over the build environment for learning purposes.", 
    "High operational overhead to maintain the Jenkins server.", 
    "Must maintain Jenkins plugins and security patches.", 
    "Reconsider if maintaining Jenkins takes too much time.")

adr7 = adr_template("007", "Argo CD for GitOps", "Accepted", 
    "Need a reliable way to deploy applications to Kubernetes.", 
    "Use Argo CD.", 
    "Flux, Jenkins Push deployments", 
    "Pull-based GitOps is more secure (no cluster credentials in CI). Argo CD provides an excellent UI.", 
    "Requires running Argo components inside the cluster.", 
    "All deployments must happen via Git commits.", 
    "Reconsider if multi-cluster management pushes us towards Flux.")

adr8 = adr_template("008", "Prometheus/Loki/Tempo Observability", "Accepted", 
    "Need monitoring, logging, and tracing.", 
    "Use the PLG stack (Prometheus, Loki, Grafana) + Tempo.", 
    "Datadog, ELK Stack, AWS CloudWatch", 
    "Open-source, highly cost-effective (Loki uses S3), avoids commercial SaaS costs.", 
    "Requires maintaining the observability stack in the cluster.", 
    "Engineers must learn LogQL and PromQL.", 
    "Reconsider if the stack consumes too many cluster resources.")

adr9 = adr_template("009", "Trivy for Security Scanning", "Accepted", 
    "Need to scan images for CVEs.", 
    "Use Trivy in CI.", 
    "Snyk, AWS Inspector", 
    "Trivy is fast, free, and accurate.", 
    "Requires CI time to download vuln databases.", 
    "Images with critical CVEs will block the build.", 
    "Reconsider if AWS Inspector provides better native integration.")

adr10 = adr_template("010", "Cosign for Image Signing", "Accepted", 
    "Need to verify image provenance.", 
    "Use Cosign.", 
    "Docker Notary", 
    "Cosign is simpler to operate, supports keyless signing.", 
    "Requires managing KMS or OIDC identities.", 
    "Images must be signed to be trusted.", 
    "Reconsider if project scope is simplified and signing is deemed unnecessary.")

adr11 = adr_template("011", "Istio Service Mesh", "Accepted", 
    "Need mTLS and advanced traffic management.", 
    "Use Istio.", 
    "Linkerd, Cilium", 
    "Istio is the industry standard with extensive features.", 
    "Steep learning curve, adds latency and resource overhead.", 
    "All pod traffic can be secured and observed.", 
    "Reconsider if the complexity causes operational issues (fallback to no mesh).")

adr12 = adr_template("012", "AI Incident Engine", "Accepted", 
    "Need intelligent RCA for production incidents.", 
    "Build a custom AI Incident Engine that reads observability data.", 
    "Commercial AIOps platforms.", 
    "Allows strict control over the safety model (human approval required for actions).", 
    "Requires custom development.", 
    "Must implement a strict allowlist and RBAC for execution.", 
    "Reconsider if AI hallucinations cause too much operational noise.")

hist1 = adr_template("HIST-001", "Redis Removal", "Historical/Removed", 
    "Redis was originally included in the architecture design.", 
    "Remove Redis.", 
    "Keep Redis for caching.", 
    "It was not actually being used by the application, adding unnecessary complexity and cost.", 
    "Cache misses will hit the DB directly.", 
    "Simplified architecture.", 
    "Reconsider if database read load becomes a bottleneck.")

hist2 = adr_template("HIST-002", "Karpenter Removal", "Historical/Removed", 
    "Needed node autoscaling.", 
    "Use EKS Managed Node Groups / Cluster Autoscaler instead of Karpenter.", 
    "Keep Karpenter.", 
    "Karpenter was too complex for the current scale of the project.", 
    "Slower node provisioning compared to Karpenter.", 
    "Simplified cluster management.", 
    "Reconsider if workload scale requires faster, more flexible node provisioning.")

hist3 = adr_template("HIST-003", "Ansible Not Core", "Historical/Removed", 
    "Considered Ansible for configuration management.", 
    "Use Terraform and GitOps (Argo CD) instead.", 
    "Use Ansible for EC2 and K8s deployments.", 
    "Terraform handles immutable infrastructure better, and GitOps is superior for K8s.", 
    "Less flexibility for OS-level mutability.", 
    "Infrastructure must be immutable.", 
    "Reconsider if we need to manage many bare-metal or non-K8s EC2 instances.")

hist4 = adr_template("HIST-004", "Route 53 Removal", "Historical/Removed", 
    "Needed DNS routing.", 
    "Remove Route 53 as a strict requirement for the core project.", 
    "Require Route 53.", 
    "Reduces cost and domain-name prerequisites for running the learning environment.", 
    "Must access services via ALB DNS names or local /etc/hosts.", 
    "Easier setup for new users.", 
    "Reconsider for a true production deployment where custom domains are required.")


write_doc("14-decisions/ADR-001-Terraform.md", adr1)
write_doc("14-decisions/ADR-002-AWS.md", adr2)
write_doc("14-decisions/ADR-003-EKS.md", adr3)
write_doc("14-decisions/ADR-004-RDS.md", adr4)
write_doc("14-decisions/ADR-005-ECR.md", adr5)
write_doc("14-decisions/ADR-006-Jenkins.md", adr6)
write_doc("14-decisions/ADR-007-Argo-CD.md", adr7)
write_doc("14-decisions/ADR-008-Observability.md", adr8)
write_doc("14-decisions/ADR-009-Security-Scanning.md", adr9)
write_doc("14-decisions/ADR-010-Cosign.md", adr10)
write_doc("14-decisions/ADR-011-Istio.md", adr11)
write_doc("14-decisions/ADR-012-AI-Incident-Engine.md", adr12)
write_doc("14-decisions/HIST-001-Redis-Removal.md", hist1)
write_doc("14-decisions/HIST-002-Karpenter-Removal.md", hist2)
write_doc("14-decisions/HIST-003-Ansible.md", hist3)
write_doc("14-decisions/HIST-004-Route-53.md", hist4)

# Create index for decisions
index_content = """# Architecture Decision Records (ADRs)

1. [ADR-001: Terraform for Infrastructure as Code](ADR-001-Terraform.md)
2. [ADR-002: AWS as Cloud Provider](ADR-002-AWS.md)
3. [ADR-003: EKS for Kubernetes](ADR-003-EKS.md)
4. [ADR-004: RDS PostgreSQL](ADR-004-RDS.md)
5. [ADR-005: ECR for Container Registry](ADR-005-ECR.md)
6. [ADR-006: Jenkins for CI](ADR-006-Jenkins.md)
7. [ADR-007: Argo CD for GitOps](ADR-007-Argo-CD.md)
8. [ADR-008: Prometheus/Loki/Tempo Observability](ADR-008-Observability.md)
9. [ADR-009: Trivy for Security Scanning](ADR-009-Security-Scanning.md)
10. [ADR-010: Cosign for Image Signing](ADR-010-Cosign.md)
11. [ADR-011: Istio Service Mesh](ADR-011-Istio.md)
12. [ADR-012: AI Incident Engine](ADR-012-AI-Incident-Engine.md)

## Historical Decisions
- [HIST-001: Redis Removal](HIST-001-Redis-Removal.md)
- [HIST-002: Karpenter Removal](HIST-002-Karpenter-Removal.md)
- [HIST-003: Ansible Not Core](HIST-003-Ansible.md)
- [HIST-004: Route 53 Removal](HIST-004-Route-53.md)
"""
write_doc("14-decisions/README.md", index_content)

print("Batch 4 written.")
