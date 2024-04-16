# PerplexiBot

An open-source, self-hosted, Discord bot, built to allow users to use GPT 3.5 Web/self-hosted Ollama models, alongside SearXNG.
Powered by https://github.com/jaypyles/FreeAskInternet-API.

Based on https://perplexity.ai

## Deployment Guide

- Create a Discord bot at https://discord.com/developers/
- Give your Bot intents to read messages and create messages

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

## Ollama Guide

Provide the `OLLAMA_MODEL` and `GPT_MODEL` environmental variables in the `perplexibot` service and add the `OLLAMA_HOST` environmental variable to the `backend` service.

```yml
perplexibot:
  container_name: perplexibot
  environment:
    - GPT_MODEL=ollama
    - OLLAMA_MODEL=orca-mini
  build:
    context: "./"
  networks:
    - search
backend:
  image: jpyles0524/freeaskinternetapi:latest
  container_name: searchbackend
  depends_on:
    - llm-freegpt35
  environment:
    - OLLAMA_HOST=http://ollama:11434
  restart: on-failure
  networks:
    - search
```
