# ADR-014: SAST for Application Security Testing in CI

**Status:** Accepted — PLANNED

---

## Context

The StockMind Jenkins CI pipeline needs a security gate that prevents known-vulnerable or insecure code from being packaged into a container image and pushed to ECR.

Two categories of application security testing exist:

- **SAST (Static Application Security Testing):** Analyses source code without executing the application.
- **DAST (Dynamic Application Security Testing):** Tests a live running application from the outside.

A decision is needed on which approach to implement, which tools to use, and when to run them in the pipeline.

---

## Decision

**Implement SAST in the Jenkins pipeline. Defer DAST to a later phase.**

SAST is implemented using four tools targeting four distinct layers:

| Tool | Layer |
|---|---|
| Bandit | Python backend source code |
| npm audit | React frontend dependencies |
| OWASP Dependency-Check | Multi-ecosystem dependency CVEs (NVD) |
| Checkov | Terraform IaC configuration |

DAST using OWASP ZAP is explicitly deferred until the GitOps test environment is stable (Phase 7+).

---

## Alternatives Considered

### Option 1: SAST only (Selected)
- Runs at source level before Docker build.
- No runtime dependency.
- Fast feedback.
- Catches the most impactful categories of vulnerability.

### Option 2: DAST only
- Tests a live application — more realistic.
- Requires a deployed running instance. At the current project stage (no stable test environment), this would mean testing against a Docker Compose stack that does not represent production.
- Slower. More complex to set up reliably.
- Misses source-level issues entirely.
- **Not selected:** Infrastructure dependency is not yet in place.

### Option 3: SAST + DAST together from day one
- Maximum coverage.
- Requires Phase 7 (GitOps + test environment) to be complete before DAST is meaningful.
- Implementing both simultaneously before the test environment exists would compromise DAST quality.
- **Not selected:** Premature. DAST will be added in a dedicated later phase.

### Option 4: SonarQube alone (no dedicated SAST tools)
- SonarQube is already planned for code quality and has some security hotspot detection.
- SonarQube is a general-purpose tool. It does not replace:
  - Bandit's Python-native security checks.
  - npm audit's native npm advisory database integration.
  - OWASP Dependency-Check's NVD-based dependency scanning.
  - Checkov's IaC-specific security rules.
- **Not selected:** SonarQube and SAST tools are complementary, not mutually exclusive.

### Option 5: Commercial tools (Snyk, Checkmarx, Veracode)
- More comprehensive, managed dashboards, less false-positive noise.
- Snyk requires an account and API token (free tier is limited).
- Checkmarx and Veracode are enterprise-licensed.
- **Not selected:** Licensing cost and external dependency are not justified for this project.

---

## Reasoning

### Why SAST before DAST:

1. **Fail-fast principle.** Catching a vulnerable dependency at the SAST stage (before Docker build) saves build time. The same issue discovered after deployment requires rollback.

2. **No infrastructure dependency.** SAST runs on source code. It works regardless of whether EKS, RDS, or any deployed environment exists.

3. **Covers the most impactful vulnerability classes.** Known CVEs in dependencies (Dependency-Check) and injection-prone code patterns (Bandit) are the most common causes of real-world application breaches.

4. **Current project phase alignment.** The pipeline is being built now. SAST is immediately usable. DAST requires Phase 7+ infrastructure.

### Why these four tools specifically:

**Bandit** — The only Python-native SAST tool. SonarQube's Python security rules are less comprehensive for Python-specific attack patterns. Zero configuration needed.

**npm audit** — Built into npm. Zero setup cost. Tests against the npm advisory database directly. No additional tool installation required.

**OWASP Dependency-Check** — Checks against the NVD (National Vulnerability Database), the authoritative global CVE registry. Complements Trivy (which scans the container image after build) by scanning at the source level before build.

**Checkov** — Finds Terraform misconfigurations that create real AWS security gaps (open security groups, unencrypted storage, overly permissive IAM). Runs on the IaC source, not the deployed infrastructure.

---

## Trade-offs

| Trade-off | Detail |
|---|---|
| False positives | All SAST tools produce false positives. Requires managing suppression files and inline annotations (`# nosec`, `checkov:skip`). |
| Build time | OWASP Dependency-Check is the heaviest (+3–8 minutes cold, ~30 seconds cached). NVD DB must be cached on the Jenkins EBS volume. |
| Not sufficient alone | SAST cannot find runtime issues. DAST must follow in a later phase for complete coverage. |
| Requires maintenance | Suppression files and tool versions must be reviewed periodically. |

---

## Consequences

- Four SAST stages are added to the Jenkins pipeline between the test stage and the Docker build stage.
- OWASP Dependency-Check NVD database is cached at `/var/jenkins_home/.dependency-check/data` on the EC2 EBS volume.
- A `dependency-check-suppressions.xml` file is created to document accepted false positives.
- A `.bandit` configuration file is created in the backend directory.
- Checkov uses `--soft-fail` initially until the baseline of findings is reviewed and suppressed or fixed.
- Bandit fails the build on HIGH severity + HIGH confidence findings.
- npm audit fails the build on HIGH or CRITICAL severity.
- OWASP Dependency-Check fails the build on CVSS score ≥ 7.0.

---

## Future Reconsideration Triggers

- When Phase 7 (GitOps + stable test namespace) is complete, re-evaluate adding OWASP ZAP DAST.
- If Bandit false positive rate becomes too high, evaluate Semgrep with custom rules as a replacement.
- If OWASP Dependency-Check cache management becomes a maintenance burden, evaluate Trivy filesystem scan as a consolidation.
- If the project requires SOC 2 or ISO 27001 compliance, re-evaluate adding a commercial SAST platform.
