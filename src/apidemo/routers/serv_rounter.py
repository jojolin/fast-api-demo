from fastapi import APIRouter

from ..services.servicedemo import ServiceDemo

router = APIRouter(prefix='/service', tags=['service', 'init_once'])


@router.get('/init_once')
def init_once():
    ServiceDemo().initialize()
    ServiceDemo().initialize()
    return {"message": "call __init__ and initialize only once"}
