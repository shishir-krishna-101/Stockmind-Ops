# ADR-001: Terraform for Infrastructure as Code

**Status:** Accepted

## Context
Need a reproducible way to provision cloud infrastructure.

## Decision
Use Terraform as the primary IaC tool.

## Alternatives Considered
CloudFormation, Pulumi, AWS CDK

## Reasoning
Terraform has broad adoption, excellent documentation, and works across providers.

## Trade-offs
Requires learning HCL and managing state files.

## Consequences
All infrastructure changes must go through code.

## Future Reconsideration Triggers
Reconsider if the team strongly prefers writing infrastructure in a general-purpose programming language (Pulumi/CDK).
