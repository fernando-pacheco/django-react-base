lint:
	blue . && isort . --profile black --line-length 79
build:
	docker compose up --build -d
db:
	docker compose up --force-recreate db