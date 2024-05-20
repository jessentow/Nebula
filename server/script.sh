#!/bin/bash

# update vm and install server
sudo yum -y update && sudo yum -y install httpd
sudo systemctl start httpd && sudo systemctl enable httpd
sudo echo "<h1>Welcome to Nebula API</h1>" > /var/www/html/index.html


# install docker
sudo yum -y install docker
sudo systemctl start docker
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -aG docker ec2-user
sudo chkconfig docker on
sudo yum install -y git
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo systemctl enable docker
sudo docker run -d -p 8000:8000 calebyeboah/nebula:1.0
sudo docker run -d -p 8080:80 nginx