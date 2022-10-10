lint:
	isort api
	black api

run:
	gunicorn --config configs/gunicorn.py --workers=1

install:
	poetry install --only main

dev_setup:
	poetry install

dev_run: lint
	uvicorn api.asgi:app --reload --host 127.0.0.1 --port 8001

