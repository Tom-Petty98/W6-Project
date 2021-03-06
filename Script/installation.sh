#!/usr/bin/env bash
 
sudo apt update -y
 
sudo apt install python3 -y
 
sudo apt install python3-pip -y
 
sudo apt install python3-venv -y

echo "Testing github webhook"
 
python3 -m venv project1-venv
 
source ~/.bashrc
 
source /var/lib/jenkins/workspace/Veggie_meals/project1-venv/bin/activate
 
cd /var/lib/jenkins/workspace/Veggie_meals
 
pip3 install -r requirements.txt
 
pytest --cov ./application
 
gunicorn --workers=4 --bind=0.0.0.0:5000 application:app