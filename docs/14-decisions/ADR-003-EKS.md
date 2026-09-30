# ADR-003: EKS for Kubernetes

**Status:** Accepted

## Context
Need a container orchestration platform.

## Decision
Use Amazon EKS.

## Alternatives Considered
Self-managed Kubernetes, ECS

## Reasoning
Reduces the operational burden of managing the control plane while maintaining K8s compatibility.

## Trade-offs
EKS control plane has a flat hourly fee.

## Consequences
Kubernetes becomes the deployment target for all workloads.

## Future Reconsideration Triggers
Reconsider if Kubernetes operational complexity outweighs benefits.
