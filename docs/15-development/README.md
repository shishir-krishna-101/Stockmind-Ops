# 15 - Development Guidelines

## Two-Repository Workflow
- **Application Code:** Make PRs against the application repository (`StockMind`).
- **Infrastructure:** Make PRs against this repository (`Stockmind-Ops`).

## Terraform Development
- Never commit `terraform.tfvars`.
- Always run `terraform fmt` before committing.
- Do not manually modify infrastructure via the AWS Console.
