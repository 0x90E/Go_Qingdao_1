#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *


class UrlLongPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "url_long")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            url_info = parse_url(url)
            '''
            URL Length < 54: Legitimate; 54 <=  URL Length <= 75: Suspicious;
            otherwice: Phishing
            '''
            url_len = len(url_info.netloc + '/' + url_info.path + '?' + url_info.params)
            if url_len < 54:
                features.append(self.R_LEGITIMATE)
            elif (54 <= url_len) and (url_len <= 75):
                features.append(self.R_SUSPICIOUS)
            else:
                features.append(self.R_PHISHING)
        return Series(features)
