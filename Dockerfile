# Use Python slim as the base image
FROM python:3.10

RUN pip install --upgrade pip && pip install pdm

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
COPY pdm.lock /app/pdm.lock
COPY ./src/perplexibot /app/perplexibot
RUN pdm install --no-lock --no-editable -vv

EXPOSE 3000

CMD [ "pdm", "run", "python", "-m", "perplexibot" ]
