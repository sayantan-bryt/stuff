import typing

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{item_id}")
async def item(item_id: typing.Union[int, str]):
    return {"message": f"Howdy partner! item_id: {item_id}"}
