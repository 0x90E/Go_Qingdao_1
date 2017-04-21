#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
import re
from com.Common.HttpRequest import *


class DomainIpPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "domain_ip")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            url_info = parse_url(url)
            domain = url_info.netloc
            ipv4 = re.match('^(\d{0,255})\.(\d{0,255})\.(\d{0,255})\.(\d{0,255})$', domain)
            ipv6 = re.match('^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|'
                            '(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|'
                            '2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|'
                            '[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|'
                            ':((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
                            '(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|'
                            '(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|'
                            '((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
                            '(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|'
                            '(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|'
                            '((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]'
                            '|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}'
                            '(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:'
                            '((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|'
                            '(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|'
                            '((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|'
                            '[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|'
                            '(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:'
                            '((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|'
                            '1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$',
                            domain)

            if ipv4 or ipv6:
                features.append(self.R_PHISHING)
            else:
                features.append(self.R_LEGITIMATE)

        return Series(features)
