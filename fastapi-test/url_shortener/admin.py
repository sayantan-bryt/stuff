from fastapi import Request
from starlette.datastructures import URL

from url_shortener import models, schemas
from url_shortener.config import get_settings


def get_admin_info(request: Request, db_url: models.URL) -> schemas.URLInfo:
    base_url = URL(get_settings().base_url)
    admin_endpoint = request.url_for(
        "administration info", secret_key=db_url.secret_key
    )
    db_url.url = str(base_url.replace(path=db_url.key))
    db_url.admin_url = str(base_url.replace(path=admin_endpoint))
    return db_url
