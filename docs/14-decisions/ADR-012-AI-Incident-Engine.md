# ADR-012: AI Incident Engine

**Status:** Accepted

## Context
Need intelligent RCA for production incidents.

## Decision
Build a custom AI Incident Engine that reads observability data.

## Alternatives Considered
Commercial AIOps platforms.

## Reasoning
Allows strict control over the safety model (human approval required for actions).

## Trade-offs
Requires custom development.

## Consequences
Must implement a strict allowlist and RBAC for execution.

## Future Reconsideration Triggers
Reconsider if AI hallucinations cause too much operational noise.
