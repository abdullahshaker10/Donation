.PHONY: run-server
run-server:
	poetry run python -m root.manage runserver 8004

.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m root.manage migrate
	
.PHONY: migrations
migrations:
	poetry run python -m root.manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m root.manage createsuperuser
	
.PHONY: update
update: install migrate ;