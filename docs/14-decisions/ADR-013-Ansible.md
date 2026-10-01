# ADR-013: Ansible for Configuration Management

**Status:** Accepted — PLANNED

---

## Context

The StockMind DevOps platform includes an EC2 instance that runs Jenkins, SonarQube, Trivy, Cosign, and supporting tools. This instance is provisioned by Terraform via a `user_data` bootstrap script (`install-ci.sh`).

While Terraform handles the **immutable infrastructure layer** (VPC, EC2 creation, IAM, security groups) and Argo CD handles the **Kubernetes application layer**, there is a third layer that neither tool is best suited for: **ongoing mutable OS-level configuration management** on EC2 instances.

The `install-ci.sh` user-data script runs only once at instance creation time. It cannot:
- Be idempotently re-applied when tools need upgrading.
- Manage Jenkins plugin installation declaratively.
- Configure SonarQube quality gates and project settings.
- Manage system-level tuning (JVM heap, open file limits, sysctl).
- Enforce configuration drift detection on the CI server.

A dedicated configuration management tool is needed for this layer.

---

## Decision

Use **Ansible** for configuration management of the Jenkins EC2 CI server and any other EC2 instances added to the platform.

**Scope of Ansible in StockMind:**

| What Ansible manages | What Ansible does NOT manage |
|---|---|
| Jenkins plugin installation and updates | AWS infrastructure (Terraform owns this) |
| SonarQube configuration and quality gate setup | Kubernetes workloads (Argo CD owns this) |
| System-level tuning (JVM heap, ulimits, sysctl) | EKS cluster resources |
| Tool version pinning and upgrades (Trivy, Cosign, AWS CLI) | RDS or other managed AWS services |
| Service health checks and restart policies | Container image building (Jenkins/Dockerfile) |
| CI server hardening (SSH, firewall rules, user management) | Application deployment |

The **ownership boundary** is clear:

```
Terraform  = Provision the EC2 instance (immutable)
Ansible    = Configure what runs on the EC2 instance (mutable)
Argo CD    = Manage Kubernetes workloads
Jenkins    = Run CI pipelines
```

---

## Alternatives Considered

### 1. Continue with user-data shell script only (`install-ci.sh`)
- **Strengths:** Already implemented, simple, no extra tooling.
- **Weaknesses:** Runs once at boot only. Cannot be re-applied idempotently. Cannot manage configuration drift. Cannot update tool versions without rebuilding the instance. Hard to test.
- **Why not selected:** The CI server needs ongoing management beyond initial provisioning.

### 2. Terraform `remote-exec` / `local-exec` provisioners
- **Strengths:** Stays within Terraform.
- **Weaknesses:** Terraform provisioners are considered a last resort. They break immutability principles. Errors are difficult to recover from. They do not replace a proper configuration management system.
- **Why not selected:** Anti-pattern for ongoing configuration management.

### 3. AWS Systems Manager (SSM) Run Command / State Manager
- **Strengths:** Native AWS, no SSH required, integrates with IAM.
- **Weaknesses:** Requires SSM agent, more complex to write and test, harder for developers to run locally, AWS-specific.
- **Why not selected:** Ansible is more portable, easier to test locally, and better known in the team's learning context.

### 4. Chef / Puppet
- **Strengths:** Mature, powerful.
- **Weaknesses:** Require dedicated server/agent infrastructure. Much higher operational overhead for a project of this scale. High learning curve.
- **Why not selected:** Overkill for this use case. Ansible is agentless.

### 5. SaltStack
- **Strengths:** Fast, good for large fleets.
- **Weaknesses:** Requires Salt master/minion setup. Complex for small-scale use.
- **Why not selected:** Same reasoning as Chef/Puppet.

---

## Reasoning

Ansible was selected because:
- **Agentless:** No agent required on the EC2 instance — uses SSH.
- **Idempotent:** Playbooks can be re-run safely. Running the same playbook twice produces the same result without unintended side effects.
- **YAML-based:** Consistent with the rest of the project's declarative approach.
- **Large ecosystem:** Ansible Galaxy has community roles for Jenkins, Docker, and system hardening.
- **Testable:** Ansible playbooks can be tested with Molecule.
- **Portfolio value:** Ansible is a core DevOps skill demonstrated alongside Terraform and GitOps.
- **Clear separation:** Ansible complements Terraform (AWS layer) and Argo CD (K8s layer) without competing with either.

---

## Trade-offs

| Trade-off | Detail |
|---|---|
| Adds another tool to the stack | Team must learn Ansible in addition to Terraform and Helm |
| Requires SSH access or SSM | Jenkins EC2 security group must allow SSH from the control machine or use SSM |
| Not real-time | Ansible is push-based — it runs on demand, not continuously like a K8s controller |
| State is implicit | Ansible does not track state the way Terraform does — drift can go undetected between runs |
| Secrets in vars | Ansible variables must be encrypted with Ansible Vault if they contain credentials |

---

## Consequences

- A new `ansible/` directory will be created in this repository.
- Ansible playbooks will codify the Jenkins CI server configuration that is currently partially handled by `install-ci.sh`.
- The `install-ci.sh` user-data script remains for initial bare-metal setup (tool installation on first boot). Ansible takes over for ongoing configuration management from that point forward.
- Sensitive values (e.g. Jenkins admin password, SonarQube token) must be stored in Ansible Vault, not plain-text YAML.
- Ansible playbooks will be documented and kept alongside the Terraform code.

---

## Future Reconsideration Triggers

- If the platform moves entirely to containerized or immutable infrastructure (e.g. Golden AMIs via Packer), Ansible's role would shrink significantly.
- If AWS SSM State Manager becomes more convenient for the team, Ansible can be replaced gradually.
- If the number of EC2 instances grows significantly, evaluate whether a more agent-based tool (Salt, Puppet) provides better scalability.
