## First Server Commands

```
sudo su
hostnamectl set-hostname BS1
yum install httpd -y
systemctl start httpd
systemctl enable httpd
vi /var/www/html/index.html
 press insert key
  Type any sentences of your choice
  press esc key press:wq
  press enter key
Copy your public ip and paste in browser
come to putty again
vi /etc/hosts
  press insert key
  34.235.151.26 BS1
  3.95.195.168  BS2
  3.91.95.202  HA
  press esc key press:wq
  press enter key
```

## Second Server Commands

```
sudo su
hostnamectl set-hostname BS2
yum install httpd -y
systemctl start httpd
systemctl enable httpd
vi /var/www/html/index.html
press insert key
Type any sentences of your choice
press esc key press:wq
press enter key
Copy your public ip and paste in browser
come to putty again
vi /etc/hosts
press insert key
34.235.151.26 BS1
3.95.195.168 BS2
3.91.95.202 HA
press esc key press:wq
press enter key
```

## HAProxy Server Commands

```
sudo su
hostnamectl set-hostname HA
yum install haproxy -y
systemctl start haproxy
systemctl enable haproxy
vi /etc/haproxy/haproxy.cfg
  press insert key then press downword arrow key
  come at the end of the file then type below lines
#############################################
frontend webapp
        bind *:80
        default_backend webserver
#################################
backend webserver
        balance roundrobin
        server  BS1 15.206.122.234:80 check
        server  BS2 35.154.106.36:80 check

press esc key press:wq
press enter key

systemctl restart haproxy
```
