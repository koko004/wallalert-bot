#!/bin/bash

# Auto Install Docker
cd ~
# Install Docker and Docker-compose
apt update && apt install docker docker-compose -y

# Download GIT
apt-get install git -y

# Folders
cd ~
mkdir WALLALERT
mkdir WALLALERT/app
mkdir WALLALERT/logs

# Download app folder
cd WALLALERT/
git clone https://github.com/koko004/wallalert-bot
mv wallalert-bot/app/* app/

# Docker-compose
docker-compose up -d --force-recreate --remove-orphans

echo "Instalacion completada"
