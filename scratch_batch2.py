from scratch_gen_docs_helper import write_doc, tech_template

net_content = """# 04 - Networking

```mermaid
flowchart TD
    Internet((Internet)) --> IGW[Internet Gateway]
    IGW --> ALB[ALB (Public Subnet)]
    ALB --> EKS_Nodes[EKS Nodes (Private Subnets)]
    EKS_Nodes --> RDS[RDS (Database Subnets)]
    EKS_Nodes --> NAT[NAT Gateway]
    NAT --> IGW
```

""" + tech_template("AWS VPC & Subnets",
    "Virtual Private Cloud providing logically isolated network space.",
    "Ensures secure communication boundaries. Isolates databases from the internet.",
    "Foundational layer for all AWS resources.",
    "IMPLEMENTED",
    "Native AWS networking boundary.",
    "Default VPC, Classic EC2",
    "Default VPC is not secure for production. Classic EC2 is deprecated.",
    "Requires careful planning of CIDR blocks.",
    "Allows strict network isolation.",
    "Requires managing route tables, subnets, and gateways.",
    "VPC is free, but NAT Gateways and data transfer incur costs.",
    "Never (fundamental to AWS).",
    "N/A"
)

tf_content = """# 05 - Terraform

```mermaid
flowchart TD
    State[(Local State)] -.-> TF[Terraform CLI]
    Code[Terraform Code CI/CD Layers] --> TF
    TF --> AWS[AWS Infrastructure]
    TF --> Argo[Argo CD Bootstrap]
```

## Repository Structure
- `terraform/CI`: CI foundations (EC2, ECR, IAM, Security Groups, VPC).
- `terraform/CD`: CD foundations (EKS, RDS, Networking, Argo CD, Load Balancer Controller).

## Missing Components / Gaps Identified
- **Remote State:** State is currently local. Needs S3 backend and DynamoDB state locking.
- **Environment Separation:** Dev/Staging/Prod workspaces or directories are not fully implemented.
- **Modules:** Monolithic files are used instead of reusable modules.
- **Tagging:** Consistent resource tagging strategy is missing.
- **CI Validation:** No automated `terraform plan` on PRs yet.

""" + tech_template("Terraform",
    "Infrastructure as Code tool.",
    "Allows repeatable, version-controlled provisioning of cloud infrastructure.",
    "Used to provision the entire AWS platform layer.",
    "IMPLEMENTED",
    "Industry standard, provider support, declarative syntax.",
    "OpenTofu, Pulumi, AWS CDK, CloudFormation, Crossplane",
    "OpenTofu is new, Pulumi/CDK change the paradigm to imperative code, CloudFormation is AWS-only, Crossplane requires a K8s cluster to bootstrap.",
    "Requires learning HCL.",
    "State file can contain secrets (must be secured).",
    "Requires state management and locking for team collaboration.",
    "Free and open-source tool, but provisions paid resources.",
    "Reconsider if the team strongly prefers writing infrastructure in Python/TypeScript (Pulumi/CDK) or if shifting entirely to Kubernetes-native provisioning (Crossplane).",
    "Rewriting all infrastructure code into another tool's syntax."
)

k8s_content = """# 06 - Kubernetes Architecture

```mermaid
flowchart TD
    Ingress[AWS ALB Ingress] --> Frontend[Frontend Service]
    Ingress --> Backend[Backend Service]
    Frontend --> PodF[Frontend Pods]
    Backend --> PodB[Backend Pods]
    PodB -.-> RDS[(RDS PostgreSQL)]
```

""" + tech_template("Amazon EKS",
    "Managed Kubernetes Service by AWS.",
    "Orchestrates containerized applications, handles scaling, self-healing, and deployments.",
    "Hosts the StockMind frontend, backend, Argo CD, and observability stack.",
    "IMPLEMENTED",
    "Reduces operational burden of managing the Kubernetes control plane.",
    "Self-managed Kubernetes (kubeadm/kops), Amazon ECS",
    "Self-managed is too complex operationally. ECS lacks the massive Cloud Native ecosystem of K8s.",
    "High baseline cost, complex IAM integration (IRSA), version upgrades require care.",
    "Control plane is managed by AWS, highly secure. Worker nodes need security hardening.",
    "Simplifies cluster lifecycle, but K8s itself remains complex.",
    "~$73/month flat fee per cluster + EC2 node costs.",
    "Reconsider if K8s proves too complex/expensive and simple container hosting (ECS/AppRunner) is sufficient.",
    "Migrating K8s manifests to ECS Task Definitions."
)

cicd_content = """# 07 - CI/CD

```mermaid
flowchart LR
    Git[GitHub] --> Jenkins[Jenkins EC2]
    Jenkins --> Test[Tests]
    Jenkins --> Lint[SonarQube]
    Jenkins --> Build[Docker Build]
    Jenkins --> Scan[Trivy]
    Jenkins --> Sign[Cosign]
    Jenkins --> Push[Push to ECR]
    Push --> GitOps[Update GitOps Repo]
```

""" + tech_template("Jenkins",
    "An open-source automation server.",
    "Automates the building, testing, scanning, signing, and pushing of container images.",
    "Runs on a dedicated EC2 instance provisioned by Terraform.",
    "PLANNED (EC2 foundation exists)",
    "Extremely flexible, large plugin ecosystem, allows full control over the execution environment.",
    "GitHub Actions, GitLab CI, AWS CodeBuild",
    "GitHub Actions is SaaS (less control over runner infrastructure in this learning context), CodeBuild is vendor-locked.",
    "Requires maintaining the Jenkins server itself (updates, plugins, security).",
    "Jenkins has full access to ECR and source code. Must be strictly secured.",
    "High operational overhead (managing the EC2 instance, JVM, plugins).",
    "Cost of the EC2 instance + EBS volume running 24/7.",
    "Reconsider if the operational burden of managing Jenkins becomes too high.",
    "Migrating Jenkinsfiles to GitHub Actions YAML workflows."
)

gitops_content = """# 08 - GitOps

```mermaid
flowchart LR
    GitRepo[GitOps Repo] --> Argo[Argo CD]
    Argo --> EKS[EKS Cluster]
    Argo --> Sync[Sync State]
```

""" + tech_template("Argo CD",
    "A declarative, GitOps continuous delivery tool for Kubernetes.",
    "Ensures the Kubernetes cluster state matches the state defined in Git.",
    "Bootstrapped by Terraform into EKS, will manage all application workloads.",
    "PARTIALLY IMPLEMENTED (Bootstrap done, apps pending)",
    "Excellent UI, deep K8s integration, industry standard for GitOps.",
    "Flux, Jenkins CD, GitHub Actions Deployment",
    "Push-based CD (Jenkins) requires granting CI access to the cluster. Flux is good but Argo's UI is superior for visibility.",
    "Requires maintaining Argo CD components inside the cluster.",
    "Extremely secure (pull-based); CI system doesn't need cluster credentials.",
    "Simplifies rollbacks and disaster recovery.",
    "Negligible (runs inside the existing EKS cluster).",
    "Reconsider if multi-cluster management becomes too complex.",
    "Migrating Argo Application manifests to Flux Kustomizations."
)

write_doc("04-networking/README.md", net_content)
write_doc("05-terraform/README.md", tf_content)
write_doc("06-kubernetes/README.md", k8s_content)
write_doc("07-cicd/README.md", cicd_content)
write_doc("08-gitops/README.md", gitops_content)

print("Batch 2 written.")
