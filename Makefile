APP_NAME = hello-world

build: ## Build the container image containing the application
	docker-compose build

run: ## Run the application capturing user console to put the input
	docker-compose up

up: build run

run_tests: ## NEED TO BE CREATED
	docker-compose run --rm  api python3 /app/tests.py
