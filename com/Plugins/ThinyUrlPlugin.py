#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin


class ThinyUrlPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "thiny_url")

    def do_extract(self, simple_data):        
        features = []
        for simple in simple_data:
            print simple
            features.append("feature_" + simple)

        return Series(features)

    def get_feature_name(self):
        return self.feature_name


        


