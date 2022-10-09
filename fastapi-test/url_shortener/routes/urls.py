import validators
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from url_shortener import crud, models, schemas
from url_shortener.admin import get_admin_info
from url_shortener.helper import get_db, raise_bad_request, raise_not_found

router = APIRouter(
    tags=["urls"],
    responses={404: {"description": "Not found"}},
)


@router.post("/url")
def create_url(url: schemas.URLBase, request: Request, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    db_url = crud.create_db_url(db=db, url=url)
    # note: should redirect
    return get_admin_info(request, db_url)


@router.get("/{url_key}")
def forward_to_target_url(
    url_key: str, request: Request, db: Session = Depends(get_db)
):
    if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
        crud.update_db_clicks(db=db, db_url=db_url)
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)
