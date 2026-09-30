# ADR-HIST-002: Karpenter Removal

**Status:** Historical/Removed

## Context
Needed node autoscaling.

## Decision
Use EKS Managed Node Groups / Cluster Autoscaler instead of Karpenter.

## Alternatives Considered
Keep Karpenter.

## Reasoning
Karpenter was too complex for the current scale of the project.

## Trade-offs
Slower node provisioning compared to Karpenter.

## Consequences
Simplified cluster management.

## Future Reconsideration Triggers
Reconsider if workload scale requires faster, more flexible node provisioning.
