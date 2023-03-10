#!/usr/bin/env bash
# set up servers for the deployment of web_static

# Install Nginx if it not already installed

sudo apt-get update 
sudo apt-get install nginx 

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#Create a fake HTML file to test nginx
echo "<html><head></head><body>Hello, World!</body></html>" | sudo tee /data/web_static/releases/test/index.html

# remove symbolic link between 2 folders 
sudo rm /data/web_static/current
# create a fsymbolic link between 2 folders 
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
# give ownership to ubuntu user and group 

sudo chown -R ubuntu:ubuntu /data/

# serve content hbnb_static using alias
sudo sed -ri "55i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-available/default
# restart nginx 
sudo service nginx restart
