#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import parse_url


class ThinyUrlPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "url_thiny")

    def do_extract(self, simple_data):        
        features = []
        for url in simple_data:
            if url[:7] == 'http://':
                url = url[7:]
            if url[:8] == 'https://':
                url = url[8:]
            url = 'http://' + url
            url_info = parse_url(url)

            if url_info.netloc.find('www.') == -1:
                features.append('1')
            else:
                features.append('0')

        return Series(features)
