# 13 - Cost Analysis

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
