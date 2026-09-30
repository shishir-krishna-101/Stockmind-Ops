# ADR-008: Prometheus/Loki/Tempo Observability

**Status:** Accepted

## Context
Need monitoring, logging, and tracing.

## Decision
Use the PLG stack (Prometheus, Loki, Grafana) + Tempo.

## Alternatives Considered
Datadog, ELK Stack, AWS CloudWatch

## Reasoning
Open-source, highly cost-effective (Loki uses S3), avoids commercial SaaS costs.

## Trade-offs
Requires maintaining the observability stack in the cluster.

## Consequences
Engineers must learn LogQL and PromQL.

## Future Reconsideration Triggers
Reconsider if the stack consumes too many cluster resources.
