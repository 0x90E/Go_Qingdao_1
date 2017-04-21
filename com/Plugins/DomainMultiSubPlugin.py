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
                features.append(self.R_LEGITIMATE)
            else:
                sub_number = len(domain_info.subdomain.split('.'))

                if sub_number == 1:
                    features.append(self.R_LEGITIMATE)
                elif sub_number == 2:
                    features.append(self.R_SUSPICIOUS)
                else:
                    features.append(self.R_PHISHING)

        return Series(features)
