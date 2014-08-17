#coding: utf-8

import argparse
from tornado import httpserver, ioloop

from server.main import application

if __name__ == "__main__":
    import logging
    logging.getLogger().setLevel(logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', dest='port', metavar="PORT", type=int, default=0)
    args = parser.parse_args()

    http_server = httpserver.HTTPServer(application, ssl_options=None, xheaders=True)
    port = args.port or 80

    http_server.listen(port)
    print('Serving on port:', port)
    ioloop.IOLoop.instance().start()