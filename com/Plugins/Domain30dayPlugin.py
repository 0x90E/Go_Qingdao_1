#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
import tldextract
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *
from com.Common.Other import *
from com.Common.ChinazQuery import ChinazQuery


class Domain30dayPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "domain_30day")

    def do_extract(self, simple_data):
        features = []
        chinaz_query = ChinazQuery()
        count = 0
        for url in simple_data:
            domain_info = tldextract.extract(url)
            domain = domain_info.domain
            if domain_info.suffix:
                domain += '.' + domain_info.suffix

            tmp_url = domain
            if domain_info.subdomain:
                tmp_url = domain_info.subdomain + "." + domain

            register_date = chinaz_query.get_domain_register_date(tmp_url)
            if register_date is None:
                features.append(0)
                continue

            register_timestamp = time.mktime(time.strptime(register_date, u'%Y年%m月%d日'))
            register_period = time.time() - register_timestamp

            print "[%s]: %s " %(tmp_url, register_period)
            features.append(register_period)
            '''
            if (time.time() - register_timestamp) < 30 * 86400:
                # < 30day
                print "[Phishing]url: %s, register date: %s" %(tmp, register_date)
                features.append('1')
            else:
                features.append('0')
                print "[legitimate]url: %s, register date: %s" %(tmp, register_date)

            count = count + 1
            '''

        return Series(features)
