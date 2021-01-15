# fast api demo
- This is just a demo project to show fast usage
- most code comes directory from [fastapi website](https://fastapi.tiangolo.com/)

## include

- async http client with [tornado.httplclient.AsyncHTTPClient](https://www.tornadoweb.org/en/stable/httpclient.html)
- async mongodb connection with [motor](https://motor.readthedocs.io/en/stable/)
- async es connection
  with [elasticsearch.AsyncElasticsearch](https://elasticsearch-py.readthedocs.io/en/7.10.0/async.html)

## usage
- require `python 3.6+`
- `pip install -r requirements.txt`
- `cd src && ADMIN_EMAIL=your-email@xx.com python -m apidemo.webserver`
- open your browser on `http://localhost:8000`
- Authorize with `user: aaa`, `password: aaa`