Terraform and HashiCorp Vault are **two different DevOps tools**, although both originated at HashiCorp and are often used together.

A simple way to remember them:

> **Terraform = builds infrastructure**
> **Vault = protects and provides secrets**

## 1. What is Terraform?

HashiCorp Terraform is an **Infrastructure as Code (IaC)** tool.

Instead of manually opening AWS/Azure/GCP and creating servers, networks, databases, load balancers, etc., you describe the infrastructure in `.tf` files.

For example:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-123456"
  instance_type = "t3.micro"
}
```

Then:

```bash
terraform init
terraform plan
terraform apply
```

Conceptually:

```text
Terraform Code
     │
     ▼
 terraform plan
     │
     ▼
 "Here is what I will create/change"
     │
     ▼
 terraform apply
     │
     ▼
AWS / Azure / GCP / Kubernetes / etc.
```

### Where Terraform is used

A DevOps engineer might receive a requirement:

> "We need a production environment with a VPC, 3 EC2 instances, an RDS database, load balancer and security groups."

Instead of creating everything manually:

```text
AWS Console
   ├── Create VPC manually
   ├── Create subnets manually
   ├── Create EC2 manually
   ├── Create RDS manually
   └── Configure security groups manually
```

you maintain Terraform code:

```text
infrastructure/
├── main.tf
├── variables.tf
├── outputs.tf
└── providers.tf
```

and Terraform creates the infrastructure.

This is valuable because the infrastructure becomes **repeatable, version-controlled and reviewable**.

---

# 2. What is HashiCorp Vault?

Vault solves a completely different problem:

> **Where should applications and engineers securely store passwords, API keys, certificates and other secrets?**

Imagine your application needs a database password.

You should generally avoid doing this:

```python
DB_USERNAME = "admin"
DB_PASSWORD = "MySecretPassword123"
```

and you definitely don't want that committed to GitHub.

Vault provides a centralized system for managing secrets.

```text
                  ┌─────────────────┐
                  │      Vault      │
                  │                 │
                  │ DB passwords    │
                  │ API keys        │
                  │ Certificates    │
                  │ Tokens          │
                  └────────┬────────┘
                           │
             authenticated requests
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
     Application       Kubernetes       CI/CD
```

An application authenticates to Vault and requests the secret it is authorized to access.

For example:

```bash
vault kv get secret/myapp/database
```

Vault might provide:

```text
username = myapp
password = ********
```

The application can use the credential without permanently hardcoding it into source code.

---

# 3. Vault can do more than store passwords

This is where Vault becomes particularly useful in larger DevOps environments.

It can handle things such as:

```text
Secrets
├── Database credentials
├── API keys
├── Cloud credentials
├── SSH credentials
├── TLS certificates
├── Encryption keys
└── Application secrets
```

It also supports **dynamic secrets**.

Instead of keeping one database password around for years, Vault can potentially generate a temporary credential.

For example:

```text
Application
     │
     │ "I need database access"
     ▼
   Vault
     │
     │ generates temporary credentials
     ▼
username: app-29382
password: ********
TTL: 1 hour
```

After the lease expires, the credentials can be revoked.

That's substantially different from simply putting a password in a `.env` file.

---

# 4. Terraform + Vault together

Now you can see why DevOps engineers might use both.

Suppose you're deploying an application to AWS.

```text
                  DevOps Engineer
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
         Terraform                Vault
             │                     │
     Creates Infrastructure     Manages Secrets
             │                     │
             ▼                     ▼
     ┌────────────────────────────────────┐
     │                AWS                 │
     │                                    │
     │ VPC                                │
     │ EC2 / EKS                          │
     │ RDS                                │
     │ Load Balancer                      │
     │ Application ───────► Secrets       │
     └────────────────────────────────────┘
```

Terraform might create:

```text
VPC
Subnets
EC2
EKS
RDS
Load Balancer
Security Groups
IAM resources
```

while Vault handles:

```text
Database passwords
API keys
Certificates
Temporary credentials
Application secrets
```

---

## 5. Terraform State creates an important connection

There's another concept you should know as you're learning Terraform: **state**.

Terraform keeps track of infrastructure using state, commonly:

```text
terraform.tfstate
```

Conceptually:

```text
Terraform configuration
        │
        ▼
   Terraform
    /       \
   ▼         ▼
Cloud      State
AWS        terraform.tfstate
```

The state tells Terraform what infrastructure it is managing.

State can contain **sensitive information**, depending on the resources and configuration. Therefore, production teams normally protect remote state carefully rather than casually committing `terraform.tfstate` to Git.

Vault doesn't automatically solve all Terraform-state security issues, but Terraform and Vault can integrate so Terraform can obtain secrets or credentials from Vault when needed. Care is still required because sensitive values can sometimes end up in Terraform state.

---

## 6. Terraform vs Ansible vs Vault

Since you've also been learning **Ansible**, this distinction is particularly useful:

| Tool          | Main purpose             | Example                              |
| ------------- | ------------------------ | ------------------------------------ |
| **Terraform** | Provision infrastructure | Create EC2, VPC, RDS                 |
| **Ansible**   | Configure systems        | Install NGINX, create users          |
| **Vault**     | Manage secrets           | DB passwords, API keys, certificates |

A realistic workflow could be:

```text
                 DevOps Engineer
                       │
                       ▼
                  Terraform
                       │
                 Creates servers
                       │
                       ▼
                     AWS
                       │
                       ▼
                   Ansible
                       │
               Configures servers
                       │
          ┌────────────┴────────────┐
          │                         │
     Install NGINX             Install App
                                    │
                                    ▼
                                  Vault
                                    │
                              Get DB secret
                                    │
                                    ▼
                                  MySQL
```

So you could think of it as:

**Terraform:**

> "Give me 5 servers."

**Ansible:**

> "Configure those 5 servers like this."

**Vault:**

> "Give those applications the secrets they're authorized to use."

That mental model will cover a large portion of what you encounter initially in DevOps.
