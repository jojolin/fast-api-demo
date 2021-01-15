from elasticsearch import AsyncElasticsearch


async def query_all(es_cli, index_name, size):
    resp = await es_cli.search(index=index_name,
                               body={"query": {"match_all": {}}},
                               size=size)
    return resp


async def go(es_host_port, index_name):
    # index_name = 'chatbot_dmservice'
    es_url = 'http://{}'.format(es_host_port)
    es_cli = AsyncElasticsearch([es_url], timeout=1)
    return await query_all(es_cli, index_name, 5)
