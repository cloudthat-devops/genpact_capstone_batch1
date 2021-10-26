resource "aws_instance" "example" {
  ami           = "ami-074cce78125f09d61"
  instance_type = "t2.micro"
    # the security group
  vpc_security_group_ids = [aws_security_group.allow-ssh.id]
  # the public SSH key
  key_name = aws_key_pair.mykeypair.key_name
  tags = {
    Name = "instance1"
  }
}



