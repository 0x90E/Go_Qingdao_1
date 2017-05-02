#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class MarqueeNumberJsPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "marquee_number_js")

    def do_extract(self, simple_data):
        features = []
        count = 0
        for values in simple_data.values:
            count = count + 1
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            try:
                if "document.write(" in soup.prettify() and "marquee" in soup.prettify():
                    features.append(1)
                    print "[marquee_number_js][Phishing] %s" %values[1]
                    continue
            except RuntimeError:
                print "RuntimeError!!"

            features.append(0)
        return Series(features)

