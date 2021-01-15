"""
mongo util
"""

import datetime

from motor.motor_asyncio import AsyncIOMotorClient


async def go(user, password, host_port, auth_db):
    mongo_url = f'mongodb://{user}:{password}@{host_port}'
    client = AsyncIOMotorClient(mongo_url, authSource=auth_db)
    await try_connect(client)
    test_db = client['test']
    test_co = test_db['co_test']
    return {"found": [f async for f in test_co.find(projection={"_id": False}, limit=3)]}


async def try_connect(client):
    test_db = client['test']
    test_co = test_db['co_test']
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    inserted = await test_co.insert_one(post)
    print(inserted.inserted_id)
