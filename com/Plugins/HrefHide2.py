#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *


class HrefHide2(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "href_hide2")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            self.read_html(values[0])

            try:
                if self.find_html('window.status') != -1 and self.find_html('statusmsg') != -1:
                    features.append(1)
                    print "[number] %d" % values[1]
                else:
                    features.append(0)
                    print "[number] %s" % values[1]
            except RuntimeError:
                print "RuntimeError!!"

        return Series(features)
