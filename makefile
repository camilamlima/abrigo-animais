ENV ?= qa
IMAGE_TAG ?= latest

export PYTHONPATH=$PYTHONPATH:./src
export SOURCE_PATH=src
export DOCKER_IMAGE_NAME=ghcr.io/camilamlima/abrigo-animais
export IMAGE_TAG ?= latest

# SET .env and override default envs
ifneq (,$(wildcard ./.env))
    include .env
	export $(shell sed 's/=.*//' .env)
endif

.PHONY: help

help:
	@grep '^[^#[:space:]].*:' $(MAKEFILE_LIST) | sort

checks: ## Runs security checks and format code
	@echo
	@poetry run isort ${SOURCE_PATH} && echo 'Isort save success!\n'
	@poetry run black ${SOURCE_PATH}  && echo 'Black save success!\n'
	@poetry run pflake8 --ignore=E701,E402 ${SOURCE_PATH}  && echo 'Flake8 check success!\n'
	@poetry run mypy --strict ${SOURCE_PATH}  && echo 'Mypy check success!\n'

dependencies: ## Installs dev dependencies
	@poetry install --no-root

shell: ## Open an python on poetry
	@poetry run python

manage: ## Run Django manage.py
	@poetry run python src/manage.py $(C)

serve-local: ## Serve application locally
	@echo "###\nStarting server...\n###\n"
	@poetry run python src/manage.py runserver

migrate: ## Run Django migrate
	@poetry run src/manage.py migrate
	
make-messages: ## Generate .po of language of django translation
	@poetry run src/manage.py makemessages -l pt_BR

compile-messages: ## Generate .mo of language of django translation
	@poetry run src/manage.py compilemessages

docker-build: ## Build docker image
	@docker build -t $(DOCKER_IMAGE_NAME):$(IMAGE_TAG) .

docker-compose-up: ## Run docker-compose up
	@docker-compose up --build