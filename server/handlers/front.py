#coding: utf-8

from .base import BaseRequestHandler

class IndexHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        self.render('')