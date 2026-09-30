# ADR-007: Argo CD for GitOps

**Status:** Accepted

## Context
Need a reliable way to deploy applications to Kubernetes.

## Decision
Use Argo CD.

## Alternatives Considered
Flux, Jenkins Push deployments

## Reasoning
Pull-based GitOps is more secure (no cluster credentials in CI). Argo CD provides an excellent UI.

## Trade-offs
Requires running Argo components inside the cluster.

## Consequences
All deployments must happen via Git commits.

## Future Reconsideration Triggers
Reconsider if multi-cluster management pushes us towards Flux.
