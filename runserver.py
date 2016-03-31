#!/usr/bin/env python

from __future__ import absolute_import
from superhttp.core.http.libhttp import *
from datetime import datetime
import optparse
import sys

parser = optparse.OptionParser()
parser.add_option("-p", dest="port", help="Port to run the server on.")
parser.add_option("-H", dest="host", help="Host to run the server on.")
parser.add_option("-d", dest="proj_dir", help="The project files that you want to deploy.")

options, args = parser.parse_args()

if __name__ == u"__main__":
    server = SuperHTTPServer((options.host, int(options.port)), RequestHandlerView)
    print u'Starting SuperHTTP web server at ' + unicode(datetime.now()) + u" on " + options.host + u":" + options.port
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Ctrl-C received. Shutting down gracefully.'
        sys.exit(0)