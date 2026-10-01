# HIST-003: Ansible as Core Deployment Mechanism — Superseded

**Status:** Superseded by [ADR-013: Ansible for Configuration Management](ADR-013-Ansible.md)

---

## Historical Context

Ansible was previously considered as a general-purpose mechanism to handle both EC2 setup and Kubernetes deployments as part of the early StockMind architecture exploration.

That approach — using Ansible as the primary deployment mechanism for application workloads — was **removed** because:

- Terraform handles AWS infrastructure provisioning better (declarative, stateful, drifts detectable).
- Argo CD (GitOps) is superior for Kubernetes workload deployment (pull-based, self-healing, UI visibility).
- Using Ansible for K8s deployments introduces push-based deployments without a clear desired-state reconciliation loop.

## Current Status

Ansible has been **re-introduced in a narrower, correct scope**: managing the ongoing mutable configuration of the Jenkins EC2 CI server — the layer that Terraform (immutable provisioning) and Argo CD (K8s layer) do not cover.

See **[ADR-013: Ansible for Configuration Management](ADR-013-Ansible.md)** for the current decision.

