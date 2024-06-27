.PHONY: build pull up destroy down logs

# --- 

build:
	 docker compose build

build-force:
	 docker compose build --no-cache

up:
	docker compose up -d --force-recreate

down:
	docker compose down

pull:
	docker compose pull

logs:
	docker compose logs
