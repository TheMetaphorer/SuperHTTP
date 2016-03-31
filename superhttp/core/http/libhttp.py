# -*- encoding: utf-8 -*-

from __future__ import absolute_import
import CGIHTTPServer, SimpleHTTPServer, BaseHTTPServer
from cgi import parse_header, parse_multipart
from urlparse import parse_qs
import json

urls = []

class RequestHandlerView(BaseHTTPServer.BaseHTTPRequestHandler):
    u"""This class is the base RequestHandler view. To create views in an app,
    subclass this and define your own get and post methods. You can also define
    a do_DELETE method, a do_PUT method, etc..."""
    headers = None

    def handle_one_request(self):
        try:
           BaseHTTPServer.BaseHTTPRequestHandler.handle_one_request(self)
           headers = self.parse_HEADERS()
        except Exception as e:
            self.do_ERROR(self, e)


    def do_GET(self):
        self.send_response(200)
        self.send_header(u"Content-type", u"text/html")
        self.end_headers()
        self.wfile.write(u"<form action=\"\" method=\"get\"><input type=\"submit\" value=\"fuck\"><input type=\"hidden\" value=\"fuck2\"></form>".encode())

    def parse_HEADERS(self):
        print self.headers
        print self.raw_requestline
        ctype, pdict = parse_header(self.headers.get(u'content-type'))
        if ctype == u'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == u'application/x-www-form-urlencoded':
            length = int(self.headers[u'content-length'])
            postvars = parse_qs(
                    self.rfile.read(length),
                    keep_blank_values=1)
        else:
            postvars = {}
        return postvars

    def do_POST(self):
        self.send_response(200)
        self.send_header(u"Content-type", u"text/html")
        self.end_headers()
        self.wfile.write(u"<form action=\"\" method=\"get\"><input type=\"submit\" value=\"fuck\"><input type=\"hidden\" value=\"fuck2\"></form>".encode())


    def do_ERROR(self, exception):
        self.wfile.write(u"An exception occured:\n ".encode() + unicode(exception).encode())



class SuperHTTPServer(BaseHTTPServer.HTTPServer):

    def serve_forever(self, poll_interval=0.5):
        BaseHTTPServer.HTTPServer.serve_forever(self, poll_interval=0.5)