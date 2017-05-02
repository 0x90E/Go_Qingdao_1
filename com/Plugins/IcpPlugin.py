#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
import tldextract
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *
from com.Common.Other import *
from com.Common.ChinazQuery import ChinazQuery


class IcpPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "icp")

    def do_extract(self, simple_data):
        features = []
        chinaz_query = ChinazQuery()
        count = 0
        for values in simple_data.values:
            count = count + 1
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue
            try:
                is_get_icp_text = False
                for text in soup.strings:
                    if "ICP" in text.upper():
                        is_get_icp_text = True
                        domain_info = tldextract.extract(values[1])
                        domain = domain_info.domain
                        if domain_info.suffix:
                            domain += '.' + domain_info.suffix

                        tmp_url = domain
                        if domain_info.subdomain:
                            tmp_url = domain_info.subdomain + "." + domain
                        icp_info = chinaz_query.get_icp_info(tmp_url)

                        if icp_info is None:
                            if u"银行" in text:
                                features.append(1)
                                print "银行 [Phishing][%s] %s" %(count, values[1])
                            else:
                                features.append(0)
                            break

                        icp_info = icp_info.split(u"号")[0]
                        if icp_info.count('-') == 2:
                            icp_info = icp_info.split("-")[1]
                        elif icp_info.count('-') == 1:
                            icp_info = icp_info.split("-")[0]

                        if icp_info in text:
                            features.append(0)
                        else:
                            features.append(1)
                            print "[Phishing][%s] %s" %(count, values[1])
                        break

            except RuntimeError:
                print "RuntimeError!!"

            if not is_get_icp_text:
                features.append(0)

        return Series(features)
