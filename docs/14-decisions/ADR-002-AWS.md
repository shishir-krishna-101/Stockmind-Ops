# ADR-002: AWS as Cloud Provider

**Status:** Accepted

## Context
Need a public cloud provider for the project.

## Decision
Use AWS.

## Alternatives Considered
GCP, Azure

## Reasoning
Familiarity with the ecosystem and availability of strong managed services like EKS and RDS.

## Trade-offs
Vendor lock-in to AWS specific services.

## Consequences
The architecture is AWS-centric.

## Future Reconsideration Triggers
Reconsider if costs become prohibitive or multi-cloud is mandated.
