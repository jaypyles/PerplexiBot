# Use Python slim as the base image
FROM python:3.10

# Update pip and install required packages
RUN pip install --upgrade pip && pip install pdm

# Set the working directory to /app
WORKDIR /app

# Copy the bot project files to the container
COPY pyproject.toml /app/pyproject.toml
COPY pdm.lock /app/pdm.lock
COPY ./src/perplexibot /app/perplexibot

# Install bot dependencies
RUN pdm install --no-lock --no-editable -vv

# Expose the bot port
EXPOSE 3000

# Start the bot
CMD [ "pdm", "run", "python", "-m", "perplexibot" ]
