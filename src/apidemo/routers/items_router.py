from fastapi import APIRouter, Depends, HTTPException

from ..dependencies.depends import get_token_header, get_query_token

from ..config import get_settings

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header), Depends(get_query_token)],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    settings = get_settings()
    print(settings)
    return "items"


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["items", "multiple_tags"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
