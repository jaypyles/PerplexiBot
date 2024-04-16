# PerplexiBot

An open-source, self-hosted, Discord bot, built to allow users to use GPT 3.5 Web alongside SearXNG.
Powered by https://github.com/jaypyles/FreeAskInternet-API.

Based on https://perplexity.ai

## Deployment Guide

- Create a Discord bot at https://discord.com/developers/

```
git clone https://github.com/jaypyles/PerplexiBot.git
cd PerplexiBot
touch .env
```

Add your bot's token to the .env file.

```
TOKEN="..."
```

`make build up`

## Example
![send](https://github.com/jaypyles/PerplexiBot/blob/master/doc/send.png)
![response](https://github.com/jaypyles/PerplexiBot/blob/master/doc/response.png)
