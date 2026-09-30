# ADR-HIST-001: Redis Removal

**Status:** Historical/Removed

## Context
Redis was originally included in the architecture design.

## Decision
Remove Redis.

## Alternatives Considered
Keep Redis for caching.

## Reasoning
It was not actually being used by the application, adding unnecessary complexity and cost.

## Trade-offs
Cache misses will hit the DB directly.

## Consequences
Simplified architecture.

## Future Reconsideration Triggers
Reconsider if database read load becomes a bottleneck.
