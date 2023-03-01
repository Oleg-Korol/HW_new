import  jinja2
from aiohttp import  web
from  aiohttp_jinja2 import setup as jinja_setup
from anet import settings

def create_app():
    app = web.Application()
    jinja_setup(
        app,
        loader = jinja2.FileSystemLoader(
            [ path/"templates"
              for path in (settings.BASE_DIR/"web").iterdir()
              if path.is_dir() and (path/"templates").exists()
              ]
        ) )
    return app

async def get_app():
    return create_app()