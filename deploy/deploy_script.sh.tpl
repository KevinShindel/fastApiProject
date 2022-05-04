#!/bin/bash

sudo apt-get update
sudo apt-get install nginx git virtualenv -y

cd /opt
mkdir ${project_name}


echo "server {
        listen 80;
        server_name localhost;
        location /static {
          alias /opt/${project_name}/static;
        }
        location / {
                proxy_set_header Host localhost;
                proxy_pass http://unix:/tmp/${project_name}.socket;
        }
}" > ${project_name}.config

sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default

sudo mv ${project_name}.config /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/${project_name}.config /etc/nginx/sites-enabled/${project_name}.config
sudo service nginx reload

sudo git clone https://${gh_token}@github.com/KevinShindel/fastApiProject ${project_name}
sudo virtualenv -p python venv
cd ${project_name}
. ../venv/bin/activate
pip install -r requirements.txt

# launch server
python -m uvicorn main:app --uds=/tmp/${project_name}.socket # run on socket