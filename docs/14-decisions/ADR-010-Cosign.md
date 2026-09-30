# ADR-010: Cosign for Image Signing

**Status:** Accepted

## Context
Need to verify image provenance.

## Decision
Use Cosign.

## Alternatives Considered
Docker Notary

## Reasoning
Cosign is simpler to operate, supports keyless signing.

## Trade-offs
Requires managing KMS or OIDC identities.

## Consequences
Images must be signed to be trusted.

## Future Reconsideration Triggers
Reconsider if project scope is simplified and signing is deemed unnecessary.
