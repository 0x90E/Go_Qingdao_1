#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
import re
import time
from com.Common.HttpRequest import *
from com.Common.Other import *


class Domain30dayPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "domain_30day")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            url_info = parse_url(url)
            domain = url_info.netloc
            """
            while True:

                content = read_html('https://www.whois.com/whois/' + domain)
                if not content:
                    print('[%s] read_html() err, try... ' % self.feature_name)
                    continue
                try:
                    partten = '(?<=Registration Date:\<\/div\>\<div class\=\"df\-value\">)' \
                              '(\d{4}-\d{1,2}-\d{1,2})(?=\<\/div>)'
                    str_reg_date0 = re.search(partten, content).group()
                except Exception, e:
                    print('[%s] No Registration Data. %s' % (self.feature_name, domain))


                list_tmp = str_reg_date0.split('-')
                reg_timestamp = time.mktime((int(list_tmp[0]), int(list_tmp[1]), int(list_tmp[2]), 0, 0, 0, 0, 0, 0))
                # print (reg_date.
                if (time.time()-reg_timestamp) < 30*86400:
                    # < 30day
                    features.append(1)
                else:
                    features.append(0)
                break
            """

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
                        features.append(self.R_PHISHING)
                    else:
                        features.append(self.R_LEGITIMATE)
                    break

        return Series(features)
