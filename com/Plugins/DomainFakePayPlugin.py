#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *
import tldextract


class DomainFakePayPlugin(AbstractPlugin):
    list_white_domain = []
    list_paywords = []

    def __init__(self):
        self.list_white_domain = read_file("com/Files/cn_white.txt").split('\n')
        self.list_paywords = 'pingan\
                            icbc\
                            ccb\
                            boc\
                            bankcomm\
                            abchina\
                            cmbchina\
                            psbc\
                            cebbank\
                            cmbc\
                            spdb\
                            ecitic\
                            cib\
                            hxb\
                            cgbchina\
                            visa\
                            citibank\
                            hsbc\
                            10086\
                            10000\
                            alipay\
                            taobao\
                            qq\
                            tenpay\
                            baifubao\
                            yeepay\
                            unionpay\
                            189\
                            epay\
                            pay'.split('\n')
        AbstractPlugin.__init__(self, "domain_fake_pay")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            domain_info = tldextract.extract(url)
            domain = domain_info.domain + '.' + domain_info.suffix
            if domain in self.list_white_domain:
                features.append('0')
                continue
            else:
                for paywords in self.list_paywords:
                    if domain.find(paywords) != -1:
                        features.append('1')
                        continue
                features.append('0')
        return Series(features)
