
resource "aws_instance" "ci" {
  ami                    = var.ami_image 
  instance_type          = var.instance_type
  subnet_id              = module.vpc.public_subnets[0]
  vpc_security_group_ids = [aws_security_group.ci.id]
  key_name               = var.key_name
  iam_instance_profile   = aws_iam_instance_profile.ci.name

  user_data = file("${path.module}/install-ci.sh")

  root_block_device {
    volume_size = 40
    volume_type = "gp3"
  }

  tags = {
    Name = "${var.project_name}-ci"
  }
}
