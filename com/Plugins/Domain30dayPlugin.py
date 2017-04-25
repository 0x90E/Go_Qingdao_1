#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *
from com.Common.Other import *
import tldextract


class Domain30dayPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "domain_30day")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            domain_info = tldextract.extract(url)
            domain = domain_info.domain
            if domain_info.suffix:
                domain += '.' + domain_info.suffix

            if trusted_domain(domain):
                features.append('0')
            else:
                while True:
                    finish, reg_timestamp = get_domain_regday(domain)
                    if finish is False:
                        print('[%s] whois err. %s, try...' % (self.feature_name, domain))
                        continue
                    if reg_timestamp is None:
                        features.append(self.R_LEGITIMATE)
                        print('[%s] No Registration Data. %s' % (self.feature_name, domain))
                        break

                    if (time.time() - reg_timestamp) < 30 * 86400:
                        # < 30day
                        features.append('1')
                    else:
                        features.append('0')
                    break

        return Series(features)
