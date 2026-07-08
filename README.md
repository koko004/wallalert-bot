
# wallalert-bot
Wallapop Search Bot

Bot de Telegram para gestionar busquedas sobre wallapop

- Notifica cuando encuentra alguna busqueda
- Avisa cuando algún ítem baja de precio
- Permite gestionar tu lista de ítems

# Docker

## Generate image docker

```bash
git clone https://github.com/koko004/wallalert-bot
docker build --tag koko004/wallalert-bot ./wallalert-bot
```

## Run on container

```bash
docker run --env BOT_TOKEN=<YOUR-TELEGRAM-BOT-TOKEN> --volume /path/to/db:/data koko004/wallalert-bot --name wallalert-bot
```

## Docker Compose
```bash
services:
  wallalert-bot:
    image: koko004/wallalert-bot
    container_name: wallalert-bot
    volumes:
      - /path/to/db:/data #Make DB persistent
    environment:
      - BOT_TOKEN=<YOUR-TELEGRAM-BOT-TOKEN>
    restart: unless-stopped
```
