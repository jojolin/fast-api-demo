"""
tornado 异步程序
"""

from tornado.httpclient import AsyncHTTPClient, HTTPRequest


async def go():
    client = AsyncHTTPClient()
    req = HTTPRequest('http://example.com/', request_timeout=2)
    resp = await client.fetch(req)
    return resp.body
