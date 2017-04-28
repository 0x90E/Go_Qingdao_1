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
        self.list_paywords = ['pingan',
                            'icbc',
                            'ccb',
                            'boc',
                            'bankcomm',
                            'abchina',
                            'cmbchina',
                            'psbc',
                            'cebbank',
                            'cmbc',
                            'spdb',
                            'ecitic',
                            'cib',
                            'hxb',
                            'cgbchina',
                            'visa',
                            'citibank',
                            'hsbc',
                            '10086',
                            '10000',
                            'alipay',
                            'taobao',
                            'qq',
                            'tenpay',
                            'baifubao',
                            'yeepay',
                            'unionpay',
                            '189',
                            'epay']
        AbstractPlugin.__init__(self, "domain_fake_pay")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            domain_info = tldextract.extract(url)
            root_domain = domain_info.domain + '.' + domain_info.suffix
            if root_domain in self.list_white_domain:
                features.append('0')
                continue
            else:
                domain = domain_info.subdomain + '.' + domain_info.domain + '.' + domain_info.suffix
                found = False
                for paywords in self.list_paywords:
                    if domain.find(paywords) != -1:
                        features.append('1')
                        found = True
                        break
                if found is False:
                    features.append('0')
        return Series(features)
