#!/usr/bin/env python

from superhttp.core.http.libhttp import *
from datetime import datetime

if __name__ == "__main__":
    server = SuperHTTPServer(('localhost', 8000), SuperHTTPRequestHandler)
    print 'Starting SuperHTTP web server at ' + str(datetime.now())
    server.serve_forever()