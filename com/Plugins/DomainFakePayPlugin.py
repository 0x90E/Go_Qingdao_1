#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *


class DomainFakePayPlugin(AbstractPlugin):
    list_white_domain = []

    def __init__(self):
        self.list_white_domain = read_file("com/Files/cn_white.txt").split('\n')
        AbstractPlugin.__init__(self, "domain_fake_pay")

    def do_extract(self, simple_data):
        """
        pingan
        icbc
        ccb
        boc
        bankcomm
        abchina
        cmbchina
        psbc
        cebbank
        cmbc
        spdb
        ecitic
        cib
        hxb
        cgbchina
        visa
        citibank
        hsbc
        10086
        10000
        alipay
        taobao
        qq
        tenpay
        baifubao
        yeepay
        unionpay
        189
        epay
        pay
        """
        features = []
        for url in simple_data:

            # features.append(str(path_depths))

        return Series(features)
