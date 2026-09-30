# ADR-011: Istio Service Mesh

**Status:** Accepted

## Context
Need mTLS and advanced traffic management.

## Decision
Use Istio.

## Alternatives Considered
Linkerd, Cilium

## Reasoning
Istio is the industry standard with extensive features.

## Trade-offs
Steep learning curve, adds latency and resource overhead.

## Consequences
All pod traffic can be secured and observed.

## Future Reconsideration Triggers
Reconsider if the complexity causes operational issues (fallback to no mesh).
