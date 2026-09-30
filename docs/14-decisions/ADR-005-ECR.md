# ADR-005: ECR for Container Registry

**Status:** Accepted

## Context
Need to store Docker images securely.

## Decision
Use Amazon ECR.

## Alternatives Considered
Docker Hub, GHCR

## Reasoning
Deep IAM integration with EKS and EC2 Jenkins host.

## Trade-offs
Vendor lock-in.

## Consequences
Images are stored securely within the AWS boundary.

## Future Reconsideration Triggers
Reconsider if migrating away from AWS.
