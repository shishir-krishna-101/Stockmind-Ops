# ADR-009: Trivy for Security Scanning

**Status:** Accepted

## Context
Need to scan images for CVEs.

## Decision
Use Trivy in CI.

## Alternatives Considered
Snyk, AWS Inspector

## Reasoning
Trivy is fast, free, and accurate.

## Trade-offs
Requires CI time to download vuln databases.

## Consequences
Images with critical CVEs will block the build.

## Future Reconsideration Triggers
Reconsider if AWS Inspector provides better native integration.
