import asyncio
import json
from functools import partial
import  python_http_parser as http_parser
from argparse import ArgumentParser
from contextlib import asynccontextmanager
from datetime import date
from asrv.web.root import urls


def get_args():
    parser = ArgumentParser(
        prog="This is server(c) {}\n\n".format(date.today().year)
    )
    parser.add_argument(
        "--port",
        default=8080,
        type=int,
        help="Port"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host")
    # return parser.parse_args()
    return parser.parse_known_args()


kn_args, ot_args = get_args()


# print(kn_args)
# print(ot_args)

async def start(app):
    print("Start Only")


async def stop1(app):
    con = app["connection"]
    print(con)
    print("Stop1 Only")


async def stop2(app):
    con = app.connection
    print(con)


async def stst1(app):
    print("Stst1 run")
    yield
    print("Stst1 end")


async def stst2(app):
    print("Stst2 run")
    yield
    print("Stst2 end")


class Controller(asyncio.Protocol):

    def connection_made(self, transport) -> None:
        self.transport = transport

    def data_received(self, data: bytes) -> None:
        print("#"*100)
        print(data.decode("utf-8"))
        req = http_parser.parse(data)
        print(dir(req))
        print(json.dumps(dict(req),indent = 4))
        # for url in urls.urlpatterns:
        #     if url[0] == req["req_uri"]:
        #         res = url[1](req)
        #         print(res)
        #         self.transport.write(res)
        self.transport.close()



class Server:
    on_start = []
    on_stop = []
    on_stst = []
    _bg_gen = []

    def __getitem__(self,item):
        return self.__dict__[item]

    def __setitem__(self,key,value):
        self.__dict__[key] = value

    @asynccontextmanager
    async def serve(self, factory):
        for cd in set(self.on_start):
            await cd(self)
        for gcb in set(self.on_stst):
            it = gcb(self).__aiter__()
            await  it.__anext__()
            self._bg_gen.append(it)
        try:
            yield await factory()
        finally:
            print("\r", end = "")
            for it in self._bg_gen[::-1]:
                try:
                    await it.__anext__()
                except StopAsyncIteration:
                    ...
            for cb in self.on_stop:
                await cb(self)
            print("Server stop")

    async def start(self):
        loop = asyncio.get_running_loop()
        _server = partial(loop.create_server, lambda: Controller(),
                          host=kn_args.host, port=kn_args.port)
        async  with self.serve(_server) as srv:
            await srv.serve_forever()

    # def start(self):
    #     self.run = True
    #     print("Server start")
    #     print("Server stop")


def run():
    srv = Server()
    srv.on_start = [start]
    srv.on_stop.extend([stop1, stop2])
    srv.on_stst.append(stst1)
    srv.on_stst.append(stst2)
    srv["connection"] = {}
    try:
        asyncio.run(srv.start())
    except KeyboardInterrupt:
        print("\rStop application")
