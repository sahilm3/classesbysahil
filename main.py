import api
import os
from aiohttp import web
import aiohttp_jinja2
import jinja2

hostx = os.getcwd()
server = api.Client()

async def main():
    app = web.Application()
    aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(hostx + '/views'))
    app.add_routes(
        [
            web.get('/', server.hello),
            web.get('/favicon.ico', server.hello),
            web.get('/{id}', server.Downloader),
            web.get('/{id}/{name}', server.Downloader),
            web.get('/{id}/name', server.name),
            web.get('/{id}/stream/{serial}', server.streamx),
        ]
    )
    return app

if __name__ == "__main__":
    web.run_app(main())