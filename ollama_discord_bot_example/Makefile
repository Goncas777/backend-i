

start:
	docker compose up --force-recreate --build -d

pull: start
	docker compose exec ollama ollama pull tinyllama:1.1b-chat-v0.6-q2_K
