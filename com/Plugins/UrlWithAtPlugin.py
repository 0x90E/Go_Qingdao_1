#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *


class UrlWithAtPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "url_with_at")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            if url.find('@') == -1:
                features.append('0')
            else:
                features.append('1')

        return Series(features)
