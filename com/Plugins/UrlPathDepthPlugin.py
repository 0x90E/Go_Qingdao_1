#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *


class UrlPathDepthPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "url_path_depth")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            url_info = parse_url(url)
            path = url_info.path
            if path and path[0] == '/':
                path = path[1:]
            if path and path[-1] == '/':
                path = path[:-1]
            path_depths = len(path.split('/'))
            features.append(str(path_depths))

        return Series(features)
