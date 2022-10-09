# Trying out FastAPI for urlshortener


### Sample `.env` file
```
ENV_NAME="Development"
BASE_URL="http://127.0.0.1:8000"
DB_URL="sqlite:///./shortener.db"
```

### How to run

```
pip3 install -r requirements.txt

uvicorn url_shortener.asgi:app --reload
```
