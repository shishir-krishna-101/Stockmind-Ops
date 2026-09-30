from scratch_gen_docs_helper import write_doc, tech_template

obs_content = """# 09 - Observability

```mermaid
flowchart TD
    App[StockMind Apps] -->|Metrics| Prom[Prometheus]
    App -->|Logs| FB[Fluent Bit]
    App -->|Traces| OTel[OpenTelemetry]
    
    FB --> Loki[Loki]
    OTel --> Tempo[Tempo]
    
    Prom --> Grafana[Grafana]
    Loki --> Grafana
    Tempo --> Grafana
    
    Prom --> Alert[Alertmanager]
```

""" + tech_template("Prometheus & Grafana",
    "Metrics monitoring and alerting toolkit + Visualization platform.",
    "Collects metrics from the cluster and applications, visualizes them, and triggers alerts.",
    "Core of the observability stack in EKS.",
    "PLANNED",
    "Industry standard for Kubernetes monitoring.",
    "AWS CloudWatch, Datadog",
    "CloudWatch is expensive for custom metrics. Datadog is commercial/expensive.",
    "Requires managing storage (EBS) and resource overhead in the cluster.",
    "Metrics can reveal business volume; Grafana must be secured via authentication.",
    "Requires tuning scrape intervals and retention to manage storage.",
    "Cost of EBS volumes for Prometheus TSDB storage.",
    "Reconsider if managing the stack becomes too burdensome and a managed service (Prometheus on AWS) is preferred.",
    "Replacing Helm charts with AWS managed Prometheus/Grafana."
) + tech_template("Fluent Bit & Loki",
    "Log processor/forwarder and log aggregation system.",
    "Collects container logs and stores them efficiently using label-based indexing.",
    "Log pipeline in EKS.",
    "PLANNED",
    "Loki is highly cost-effective (stores in S3, minimal indexing) compared to Elasticsearch.",
    "Elasticsearch/Fluentd/Kibana (EFK), Vector, OpenSearch",
    "EFK/OpenSearch is very resource-intensive (JVM memory, heavy indexing).",
    "Loki queries (LogQL) are less flexible for full-text search without labels.",
    "Logs must not contain sensitive PII (requires masking in Fluent Bit).",
    "Fluent Bit is very lightweight.",
    "Highly cost-effective due to S3 backend for Loki.",
    "Reconsider if complex full-text analytics are required.",
    "Migrating to OpenSearch."
)

sec_content = """# 10 - Security

```mermaid
flowchart TD
    Dev[Developer] --> GitHub
    GitHub --> Jenkins
    Jenkins --> Trivy[Trivy Vulnerability Scan]
    Trivy --> Cosign[Cosign Image Signing]
    Cosign --> ECR
    
    EKS --> OPA[Policy Enforcement]
```

""" + tech_template("Trivy & Cosign",
    "Container vulnerability scanner and OCI artifact signing tool.",
    "Ensures images are free of known CVEs and cryptographically verifies image provenance.",
    "Jenkins CI pipeline.",
    "PLANNED",
    "Trivy is fast and accurate; Cosign uses keyless signing and OIDC.",
    "Snyk, Grype, AWS Inspector, Docker Notary",
    "Snyk is commercial. AWS Inspector is AWS-specific. Notary is overly complex.",
    "Build times increase.",
    "Prevents deployment of compromised or untrusted images.",
    "Requires managing signing keys (KMS) or OIDC identities.",
    "Trivy/Cosign are free open-source tools.",
    "Reconsider if shifting to AWS native security (Inspector).",
    "Replacing Jenkins stages with AWS Inspector automated scanning."
)

ai_content = """# 11 - AI Incident Engine

```mermaid
flowchart TD
    Alert[Prometheus Alert] --> Engine[AI Incident Engine]
    Loki[Loki Logs] --> Engine
    Tempo[Tempo Traces] --> Engine
    
    Engine --> RCA[Root Cause Analysis]
    Engine --> Rec[Recommendation]
    
    Rec --> Human[Human Approval]
    Human -- Approve --> Remediation[Allowlisted Action e.g. Restart Pod]
```

## Safety Model
The AI Incident Engine must **never** have unrestricted Kubernetes cluster access.
- Read access to observability data only.
- Output is an RCA report and a suggested action.
- Execution requires a separate, hardened executor component.
- The executor only performs predefined, allowlisted actions (e.g., `restart`, `scale`, `rollback`).
- A human must explicitly approve the action via an interface before the executor runs it.
"""

ops_content = """# 12 - Operations

## Incident Response
1. **Detect:** Alerts fire from Prometheus/Alertmanager.
2. **Triage:** Check Grafana dashboards.
3. **Investigate:** (Future) AI Incident Engine provides RCA; otherwise manual LogQL/TraceQL queries.
4. **Remediate:** Rollback via Argo CD or restart workloads.
5. **Review:** Post-incident review.

## Disaster Recovery
- **Infrastructure:** Reprovision via Terraform.
- **Application State:** GitOps (Argo CD) will automatically redeploy applications.
- **Database:** AWS RDS automated backups allow point-in-time recovery.
"""

cost_content = """# 13 - Cost Analysis

## Cost Optimization Strategies
- **Right-sizing:** Monitor EKS node CPU/Memory usage and select appropriate instance types.
- **Autoscaling:** Implement HPA/Cluster Autoscaler to scale down at night.
- **Spot Instances:** Use Spot instances for CI Jenkins node and stateless EKS workloads.
- **ECR Lifecycle:** Delete untagged or old images automatically.
- **NAT Optimization:** Consolidate to one NAT Gateway for the entire VPC (learning/dev environment) rather than per-AZ.

## Cost Model Formulas
- `Monthly EC2 = instance hourly price × hours running`
- `Monthly RDS = (instance cost × hours) + (storage GB × rate) + backup storage`
- `Monthly EKS = (control plane $0.10/hr × 730) + Node EC2 costs`
- `Monthly NAT = ($0.045/hr × 730) + (Data processed GB × $0.045)`
- `Monthly AI = (Requests × Avg Tokens/Req) × API Provider Rate`

## Scenarios
1. **Learning Environment (Current State):** Minimal EC2, Single NAT, Single AZ RDS. Estimated $100-$150/mo.
2. **Medium Workload:** Multi-AZ RDS, 3+ EKS nodes. Estimated $300-$500/mo.
"""

dev_content = """# 15 - Development Guidelines

## Two-Repository Workflow
- **Application Code:** Make PRs against the application repository (`StockMind`).
- **Infrastructure:** Make PRs against this repository (`Stockmind-Ops`).

## Terraform Development
- Never commit `terraform.tfvars`.
- Always run `terraform fmt` before committing.
- Do not manually modify infrastructure via the AWS Console.
"""

write_doc("09-observability/README.md", obs_content)
write_doc("10-security/README.md", sec_content)
write_doc("11-ai-incident-engine/README.md", ai_content)
write_doc("12-operations/README.md", ops_content)
write_doc("13-cost/README.md", cost_content)
write_doc("15-development/README.md", dev_content)

print("Batch 3 written.")
