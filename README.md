![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/koko004/wallalert) [![Docker pulls](https://img.shields.io/docker/pulls/koko004/wallalert?style=flat-square)](https://hub.docker.com/r/koko004/wallalert)  [![commit_freq](https://img.shields.io/github/commit-activity/m/koko004/wallalert?style=flat-square)](https://github.com/koko004/wallalert/commits) [![Build Status](https://travis-ci.com/koko004/wallalert.svg)](https://travis-ci.com/koko004/wallalert)  [![last_commit](https://img.shields.io/github/last-commit/koko004/wallalert?style=flat-square)](https://github.com/koko004/wallalert/commits) ![Docker Image Version (latest by date)](https://img.shields.io/docker/v/koko004/wallalert) ![GitHub](https://img.shields.io/github/license/koko004/wallalert)


# wallalert-bot v2.4
wallapop search bot

bot de Telegram para gestionar busquedas sobre wallapop

- Notifica cuando encuentra alguna busqueda
- Avisa cuando algún ítem baja de precio
- Permite gestionar tu lista de ítems

pip3 install -r requirements.txt

# Docker

## Docker compose

```bash
version: '3.3'
services:
    wallbot-docker:
        image: koko004/wallalert:armv7
        container_name: wallabot
        restart: always
        environment:
            - BOT_TOKEN=TOKEN
        volumes:
          - ~/WALLALERT/app:/app
          - ~/WALLALERT/logs:/logs
```

## Generate image docker

```bash
docker build --tag koko004/wallalert:latest .
```

## Tag version

###### Windows
```ps
$version = Get-Content "VERSION"
```
###### Unix
```bash
version=`cat VERSION`
```

###### Tag
```bash
docker tag koko004/wallalert:latest koko004/wallalert:$version
```
###### Push
```bash
docker push koko004/wallalert:latest 
docker push koko004/wallalert:$version
```
## See images

```bash
docker images
```

## Run on container

```bash
docker run --env BOT_TOKEN=<YOUR-TOKEN> koko004/wallalert:latest --name wallalert-bot
```

## Export image
```bash
docker save -o wallalert.tar koko004/wallalert:latest
```
