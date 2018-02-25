#!/usr/bin/env bash

# upgrade all
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get -y upgrade

# install basic python dependencies - https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04
sudo apt-get install build-essential libssl-dev libffi-dev python-dev --yes

# install python - https://snakeycode.wordpress.com/2017/11/18/working-in-python-3-6-in-ubuntu-14-04/
sudo apt-get install python3.6 --yes
rm -f /home/vagrant/.bash_profile

# avoid creating .pyc files
echo 'export PYTHONDONTWRITEBYTECODE=1' >> /home/vagrant/.bash_profile

# alias to make life easier
echo 'alias python=python3.6' >> /home/vagrant/.bash_profile

# load pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3.6 get-pip.py
sudo python3.6 setup.py install

