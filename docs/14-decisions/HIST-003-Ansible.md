# ADR-HIST-003: Ansible Not Core

**Status:** Historical/Removed

## Context
Considered Ansible for configuration management.

## Decision
Use Terraform and GitOps (Argo CD) instead.

## Alternatives Considered
Use Ansible for EC2 and K8s deployments.

## Reasoning
Terraform handles immutable infrastructure better, and GitOps is superior for K8s.

## Trade-offs
Less flexibility for OS-level mutability.

## Consequences
Infrastructure must be immutable.

## Future Reconsideration Triggers
Reconsider if we need to manage many bare-metal or non-K8s EC2 instances.
