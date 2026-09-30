# ADR-006: Jenkins for CI

**Status:** Accepted

## Context
Need a CI server for building and scanning images.

## Decision
Use Jenkins on a dedicated EC2 instance.

## Alternatives Considered
GitHub Actions, GitLab CI

## Reasoning
Provides full control over the build environment for learning purposes.

## Trade-offs
High operational overhead to maintain the Jenkins server.

## Consequences
Must maintain Jenkins plugins and security patches.

## Future Reconsideration Triggers
Reconsider if maintaining Jenkins takes too much time.
