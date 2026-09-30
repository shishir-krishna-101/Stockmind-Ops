# 12 - Operations

## Incident Response
1. **Detect:** Alerts fire from Prometheus/Alertmanager.
2. **Triage:** Check Grafana dashboards.
3. **Investigate:** (Future) AI Incident Engine provides RCA; otherwise manual LogQL/TraceQL queries.
4. **Remediate:** Rollback via Argo CD or restart workloads.
5. **Review:** Post-incident review.

## Disaster Recovery
- **Infrastructure:** Reprovision via Terraform.
- **Application State:** GitOps (Argo CD) will automatically redeploy applications.
- **Database:** AWS RDS automated backups allow point-in-time recovery.
