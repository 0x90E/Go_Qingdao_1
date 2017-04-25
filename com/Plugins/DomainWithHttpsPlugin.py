#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *


class DomainWithHttpsPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "domain_with_https")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            url_info = parse_url(url)
            if url_info.netloc.lower().find('https') == -1:
                features.append('0')
            else:
                features.append('1')

        return Series(features)
