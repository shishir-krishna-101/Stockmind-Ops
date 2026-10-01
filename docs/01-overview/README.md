# 01 - Project Overview

StockMind is an AI-assisted inventory-management / inventory intelligence application.

## 1. What is StockMind?
A full-stack application backed by modern DevOps practices, providing businesses with visibility into their inventory, low-stock detection, demand prediction, and stockout-risk analysis.

## 2. Why does StockMind exist?
1. To solve the business problem of turning raw inventory/sales data into actionable insights and forecasts.
2. To serve as a realistic platform for demonstrating practical cloud infrastructure, containerization, Infrastructure-as-Code (Terraform), CI/CD, GitOps, observability, and advanced AI-assisted operations.

## 3. Two-Repository Model
The project enforces a strict separation of concerns:
- **Application Repository** (`https://github.com/shishir-krishna-101/StockMind.git`): Contains the React frontend, FastAPI backend, and application-level tests.
- **DevOps Repository** (`Stockmind-Ops`): Contains the Terraform AWS infrastructure, Argo CD bootstrapping, CI configuration, and this documentation.

This separation ensures that developers focus on application logic while platform engineers manage infrastructure state without cross-contamination of secrets or concerns.

---

## 4. Where to Start

For a complete step-by-step guide covering all phases from prerequisites to the AI Incident Engine, see the **[Complete Setup Guide](SETUP_GUIDE.md)**.

The setup guide covers:
- **Phase 1 & 2:** Terraform CI/CD Foundation — `IMPLEMENTED, start here`
- **Phase 3–6:** Containerization, first EKS deployment, Jenkins CI, security scanning
- **Phase 7:** Argo CD GitOps
- **Phase 8–10:** Observability, autoscaling, security hardening
- **Phase 11–13:** AI Incident Engine, controlled remediation, cost optimization
