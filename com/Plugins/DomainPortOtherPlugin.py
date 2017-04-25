#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *


class DomainPortOtherPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "domain_port_other")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            url_info = parse_url(url)
            if url_info.port == 80 or url_info.port == 443 or url_info.port is None:
                features.append('0')
            else:
                features.append('1')

        return Series(features)
