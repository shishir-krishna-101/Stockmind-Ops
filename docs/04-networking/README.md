# 04 - Networking

```mermaid
flowchart TD
    Internet((Internet)) --> IGW[Internet Gateway]
    IGW --> ALB[ALB (Public Subnet)]
    ALB --> EKS_Nodes[EKS Nodes (Private Subnets)]
    EKS_Nodes --> RDS[RDS (Database Subnets)]
    EKS_Nodes --> NAT[NAT Gateway]
    NAT --> IGW
```

## AWS VPC & Subnets

### 1. What is it?
Virtual Private Cloud providing logically isolated network space.

### 2. What problem does it solve?
Ensures secure communication boundaries. Isolates databases from the internet.

### 3. Where is it used in StockMind?
Foundational layer for all AWS resources.

### 4. Is it implemented or planned?
**Status:** IMPLEMENTED

### 5. Why was it selected?
Native AWS networking boundary.

### 6. What alternatives were considered?
Default VPC, Classic EC2

### 7. Why were those alternatives not selected?
Default VPC is not secure for production. Classic EC2 is deprecated.

### 8. What are the trade-offs?
Requires careful planning of CIDR blocks.

### 9. What are the security implications?
Allows strict network isolation.

### 10. What are the operational implications?
Requires managing route tables, subnets, and gateways.

### 11. What are the cost implications?
VPC is free, but NAT Gateways and data transfer incur costs.

### 12. When should we reconsider it?
Never (fundamental to AWS).

### 13. What would replacing it look like?
N/A


