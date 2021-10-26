# capstone

Task 1:
Using Terraform launch an EC2 instance with security group corresponding to web-application. Using the terraform created instance and ansible install web-server (httpd) in that instance. Make sure the webs-server is up and running.

Install terraform using following commands

$ sudo apt update
$ sudo apt install wget unzip -y
$ wget https://releases.hashicorp.com/terraform/1.0.9/terraform_1.0.9_linux_amd64.zip
$ unzip terraform_1.0.9_linux_amd64.zip
$ sudo mv terraform /usr/local/bin

install the aws cli

$ sudo apt-get install python3-pip -y
$ sudo pip3 install awscli 

use aws configure and give your credentials

create a directory and inside that directory create your terraform files to create a instance

Also remember to create key pair using 

$ ssh-keygen -f mykey

Finally use terraform init, fmt, validate, plan & apply to create your instance

** Make sure to modify your ami depending upon region and instance you need. Also modify the VPC id **

Once you have created instance using terraform ssh into that instance and install ansible in it

Install the ansible using the following commands

$ sudo yum check-update
$ sudo yum install python3.8 wget -y
$ sudo pip3 install awscli boto boto3 ansible
$ ansible --version

use aws configure and give your credentials

Create a inventory in the location /etc/ansible/hosts

** localhost ansible_connection=local **

create a directory and inside that directory create your ansible playbook to install httpd webserver

use ansible-playbook <playbook name.yaml> 
  
Make sure the webserver is running
  
Task 2:
Build a docker image to use the python api and push it to the DockerHub. Create a pod and nodeport service with that Docker image.
  
  Hint: A KOPS cluster would be provided to you. You can use the worker nodes to write DockerFile and build image
  Hint: Use the DockerFile provided to you if needed to create the docker image
 
Create the DockerFile, requirements.txt and python api code in the same directory. use the following commands to build the image and push it to docker hub
  
$ docker login -u <username>
$ docker build -t <username>/test-flask-app:v1 . 
$ docker push <username>/test-flask-app:v1

In the jumper node create a pod that uses the above created image. Use the pod.yaml file.
  
Use the following command to create the pod and a service for that pod
  
$ kubectl apply -f <pod name.yaml>
$ kubectl expose po <pod name> --type NodePort --port 5000
$ kubectl get svc

Use the public Ip of the worker nodes and nodeport number to access in web page
                      
 
  






