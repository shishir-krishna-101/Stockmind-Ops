output "ci_instance_id" {
  value = aws_instance.ci.id
}

output "ci_public_ip" {
  value = aws_instance.ci.public_ip
}

output "jenkins_url" {
  value = "http://${aws_instance.ci.public_ip}:8080"
}

output "sonarqube_url" {
  value = "http://${aws_instance.ci.public_ip}:9000"
}

output "ecr_frontend_url" {
  value = aws_ecr_repository.frontend.repository_url
}

output "ecr_backend_url" {
  value = aws_ecr_repository.backend.repository_url
}

output "ecr_ai_incident_engine_url" {
  value = aws_ecr_repository.ai_incident_engine.repository_url
}
