#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
import tldextract


class DomainSubNumberPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "domain_sub_number")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            domain_info = tldextract.extract(url)
            if domain_info.subdomain == '':
                features.append('0')
            else:
                features.append(len(domain_info.subdomain.split('.')))

        return Series(features)
