from fastapi import FastAPI

from url_shortener import models
from url_shortener.database import engine
from url_shortener.routes import admin, items, urls

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items.router)
app.include_router(urls.router)
app.include_router(
    admin.router,
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Ho Hey!"}
