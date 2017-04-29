#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *


class ElementHide(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "element_hide")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            self.read_html(values[0])

            try:
                found_count_1 = self.value_count("display:none")
                found_count_2 = self.value_count('display:"none"')
                if found_count_1 > found_count_2:
                    features.append(found_count_1)
                    print "[number] %d" % found_count_1
                else:
                    features.append(found_count_2)
                    print "[number] %s" % found_count_2
            except RuntimeError:
                print "RuntimeError!!"

        return Series(features)
