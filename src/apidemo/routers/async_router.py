from typing import Optional

from fastapi import APIRouter
from ..asyncdemo import http_async, mongo_async, es_async

router = APIRouter(prefix='/async', tags=['async'])


@router.get('/http')
async def http():
    return await http_async.go()


@router.get('/mongo')
async def mongo(user, password, host_port, auth_db: Optional[str] = 'test'):
    return await mongo_async.go(user, password, host_port, auth_db)


@router.get('/es')
async def es(es_host_port: str, index_name: str):
    return await es_async.go(es_host_port, index_name)
