#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
import tldextract


class UrlIncludeAspPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "url_include_asp")

    def do_extract(self, simple_data):
        features = []
        count = 0
        for url in simple_data:
            count = count + 1
            if ".asp" in url:
                features.append(1)
                print "[Dark][url_include_asp][%s]: %s" %(count,url)
            else:
                features.append(0)

        return Series(features)

