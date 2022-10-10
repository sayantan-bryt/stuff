workers = 1
worker_class = "uvicorn.workers.UvicornWorker"

bind = ["127.0.0.1:8001"]
timeout = 60

accesslog = "-"
errorlog = "-"

wsgi_app = "api.asgi:app"
