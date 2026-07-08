[![commit_freq](https://img.shields.io/github/commit-activity/m/IceFox2/wallbot?style=flat-square)](https://github.com/IceFox2/wallbot/commits) [![last_commit](https://img.shields.io/github/last-commit/IceFox2/wallbot?style=flat-square)](https://github.com/IceFox2/wallbot/commits) ![GitHub](https://img.shields.io/github/license/IceFox2/wallbot)


# Wallbot
Wallapop Search Bot

Bot de Telegram para gestionar busquedas sobre wallapop

- Notifica cuando encuentra alguna busqueda
- Avisa cuando algún ítem baja de precio
- Permite gestionar tu lista de ítems

# Docker

## Generate image docker

```bash
git clone https://github.com/IceFox2/wallbot
docker build --tag IceFox2/wallbot-docker:1.0.7 ./wallbot
```

## Run on container

```bash
docker run --env BOT_TOKEN=<YOUR-TELEGRAM-BOT-TOKEN> --volume /path/to/db:/data IceFox2/wallbot-docker:1.0.7 --name wallbot
```

## Docker Compose
```bash
services:
  wallbot:
    image: IceFox2/wallbot-docker:1.0.7
    container_name: wallbot
    volumes:
      - /path/to/db:/data #Make DB persistent
    environment:
      - BOT_TOKEN=<YOUR-TELEGRAM-BOT-TOKEN>
    restart: unless-stopped
```