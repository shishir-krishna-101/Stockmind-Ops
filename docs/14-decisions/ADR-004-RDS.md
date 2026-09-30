# ADR-004: RDS PostgreSQL

**Status:** Accepted

## Context
Need a reliable relational database for the application.

## Decision
Use managed Amazon RDS PostgreSQL.

## Alternatives Considered
Self-hosted PostgreSQL in K8s, Aurora

## Reasoning
RDS handles backups, patching, and high availability without K8s statefulset complexity. PostgreSQL was chosen over MySQL for JSON support and advanced features.

## Trade-offs
Higher cost than self-hosting.

## Consequences
Database state is externalized from the Kubernetes cluster.

## Future Reconsideration Triggers
Reconsider if database costs are too high, requiring self-hosting.
