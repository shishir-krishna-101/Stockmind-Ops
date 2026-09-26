# StockMind CD Terraform — GitOps

This is the CD-side Terraform foundation for the StockMind GitOps architecture.

## Terraform owns

- VPC
- Public/private/database subnets
- One NAT Gateway for the dev setup
- EKS cluster
- EKS managed node group
- EKS add-ons
- RDS PostgreSQL
- AWS Secrets Manager application secret
- IAM/IRSA role for AWS Load Balancer Controller
- AWS Load Balancer Controller Helm release
- IAM/IRSA role for External Secrets Operator
- Argo CD bootstrap installation

## Argo CD owns after bootstrap

The GitOps repository should manage the Kubernetes platform and workloads:

- External Secrets Operator
- StockMind frontend
- StockMind backend
- AI Incident Engine
- Istio
- Prometheus
- Grafana
- Alertmanager
- Loki
- Fluent Bit
- OpenTelemetry
- Tempo

The important ownership boundary is:

Terraform = AWS infrastructure + IAM + Argo CD bootstrap

Argo CD = Kubernetes platform + applications

Jenkins = CI only; build, test, scan, sign and push images, then update the GitOps repository.

## Flow

```text
Application GitHub
        |
        v
     Jenkins
        |
        +--> Test
        +--> SonarQube
        +--> Docker build
        +--> Trivy
        +--> Cosign
        +--> ECR
        |
        +--> update GitOps repo
                    |
                    v
             Argo CD on EKS
                    |
                    v
              Kubernetes
        +-----------+-----------+
        |           |           |
     StockMind  Platform   Observability
```

## Run

```bash
cp terraform.tfvars.example terraform.tfvars

terraform init
terraform fmt -recursive
terraform validate
terraform plan
terraform apply
```

Do not commit `terraform.tfvars`.

## After Terraform

The GitOps repository needs to contain the Argo CD Application definitions
for the Kubernetes components. Argo CD can then sync those components.

This stack intentionally does NOT install the AWS Load Balancer Controller,
Istio, Prometheus, Grafana, Loki, Fluent Bit, OpenTelemetry, Tempo or
StockMind through Terraform. Those belong in GitOps.

## Note

The AWS Load Balancer Controller is installed by Terraform in `argocd.tf`.
Terraform creates its IAM/IRSA role and Kubernetes ServiceAccount, then
installs the controller Helm chart into `kube-system`.
