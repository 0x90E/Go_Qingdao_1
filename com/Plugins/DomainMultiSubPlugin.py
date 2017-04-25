#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
import tldextract


class DomainMultiSubPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "domain_multi_sub")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            domain_info = tldextract.extract(url)

            if domain_info.subdomain == '':
                features.append('0')
            else:
                sub_number = len(domain_info.subdomain.split('.'))
                features.append(str(sub_number))

        return Series(features)
