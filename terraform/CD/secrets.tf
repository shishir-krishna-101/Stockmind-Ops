resource "aws_secretsmanager_secret" "application" {
  name = "${var.project_name}/${var.environment}/application"

  tags = {
    Name = "${var.project_name}/${var.environment}/application"
  }
}

resource "aws_secretsmanager_secret_version" "application" {
  secret_id = aws_secretsmanager_secret.application.id

  secret_string = jsonencode({
    GEMINI_API_KEY = var.gemini_api_key
    JWT_SECRET     = var.jwt_secret
  })
}
