#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
import tldextract
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *
from com.Common.Other import *
from com.Common.ChinazQuery import ChinazQuery
from com.Common.AsyncTask import AsyncTask


class Domain30dayPlugin(AbstractPlugin):

    chinaz_query = None

    def __init__(self):
        AbstractPlugin.__init__(self, "domain_30day")
        self.chinaz_query = ChinazQuery()

    def _request_callback(self, domain):
        self.chinaz_query.get_domain_register_date(domain)
        print("[ready cache]: get_domain_register_date(%s) " % domain)
        pass

    def do_extract(self, simple_data):
        features = []

        count = 0

        # whois_cache ==> begin
        list_params = []
        for url in simple_data:
            domain_info = tldextract.extract(url)
            domain = domain_info.domain
            if domain_info.suffix:
                domain += '.' + domain_info.suffix
            list_params.append(domain)
        async_task = AsyncTask(10, self._request_callback)
        async_task.append_task(list_params)
        async_task.wait()
        # end

        for url in simple_data:
            domain_info = tldextract.extract(url)
            domain = domain_info.domain
            if domain_info.suffix:
                domain += '.' + domain_info.suffix

            # tmp_url = domain
            # if domain_info.subdomain:
            #     tmp_url = domain_info.subdomain + "." + domain

            register_date = self.chinaz_query.get_domain_register_date(domain)
            if register_date is None:
                features.append(self.R_NONE)
                continue

            register_timestamp = time.mktime(time.strptime(register_date, u'%Y年%m月%d日'))
            register_period = time.time() - register_timestamp

            print "[%s]: %s " % (domain, register_period)
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
