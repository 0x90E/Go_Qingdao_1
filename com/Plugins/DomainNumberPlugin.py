#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
import re
from com.Common.HttpRequest import *


class DomainNumberPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "domain_number")

    def do_extract(self, simple_data):
        features = []
        for url in simple_data:
            url_info = parse_url(url.lower())
            list_domain = re.findall('((?=(http://|https://|=|/)*)(([a-z0-9\-_]+?\.)*?)([a-z0-9\-_]+?)'
                                     '(\.biz|\.com|\.edu|\.gov|\.info|\.int|\.mil|\.name|\.net|\.org|\.pro|\.xxx|'
                                     '\.top|\.site|\.men|\.host|\.space|\.racing|\.wiki|\.pub|\.guru|\.ren|\.win|'
                                     '\.club|\.xyz|\.global|\.futbol|\.guru|\.tech|\.bid|\.rocks|\.wang|\.webcam|'
                                     '\.porn|\.loan|\.trade|\.science|\.date|\.taipei|\.news|\.rs|\.video|\.vip|'
                                     '\.click|\.petrochina|\.today|\.store|\.ru|\.faith|\.cool|\.online|\.lol|'
                                     '\.aero|\.cat|\.coop|\.jobs|\.museum|\.travel|\.mobi|\.asia|\.tel|\.arpa|\.root|'
                                     '\.tel|\.post|\.geo|\.kid|\.mail|\.sco|\.web|\.nato|\.example|\.invalid|'
                                     '\.localhost|\.test|\.bitnet|\.csnet|\.local|\.onion|\.uucp|Others|\.ac|\.ad|'
                                     '\.ae|\.af|\.ag|\.ai|\.al|\.am|\.an|\.ao|\.aq|\.ar|\.as|\.at|\.au|\.aw|\.az|\.ba|'
                                     '\.bb|\.bd|\.be|\.bf|\.bg|\.bh|\.bi|\.bj|\.bm|\.bn|\.bo|\.br|\.bs|\.bt|'
                                     '\.bv|\.bw|\.by|\.bz|\.ca|\.cc|\.cd|\.cf|\.cg|\.ch|\.ci|\.ck|\.cl|\.cm|\.cn|'
                                     '\.co|\.cr|\.cu|\.cv|\.cx|\.cy|\.cz|\.de|\.dj|\.dk|\.dm|\.dz|\.ec|\.ee|\.eg|'
                                     '\.er|\.es|\.et|\.eu|\.fi|\.fj|\.fk|\.fm|\.fo|\.fr|\.ga|\.gd|\.ge|\.gf|\.gg|\.gh|'
                                     '\.gi|\.gl|\.gm|\.gn|\.gp|\.gq|\.gr|\.gs|\.gt|\.gu|\.gw|\.gy|\.hk|\.hm|\.hn|\.hr|'
                                     '\.ht|\.hu|\.id|\.ie|\.il|\.im|\.in|\.io|\.iq|\.ir|\.is|\.it|\.je|\.jm|\.jo|\.jp|'
                                     '\.ke|\.kg|\.kh|\.ki|\.km|\.kn|\.kr|\.kw|\.ky|\.kz|\.la|\.lb|\.lc|\.li|\.lk|\.lr|'
                                     '\.ls|\.lt|\.lu|\.lv|\.ly|\.ma|\.mc|\.md|\.me|\.mg|\.mh|\.mk|\.ml|\.mm|\.mn|\.mo|'
                                     '\.mp|\.mq|\.mr|\.ms|\.mt|\.mu|\.mv|\.mw|\.mx|\.my|\.mz|\.na|\.nc|\.ne|\.nf|\.ng|'
                                     '\.ni|\.nl|\.no|\.np|\.nr|\.nu|\.nz|\.om|\.pa|\.pe|\.pf|\.pg|\.ph|\.pk|\.pl|\.pm|'
                                     '\.pn|\.pr|\.ps|\.pt|\.pw|\.py|\.qa|\.re|\.ro|\.ru|\.rw|\.sa|\.sb|\.sc|\.sd|\.se|'
                                     '\.sg|\.sh|\.si|\.sk|\.sl|\.sm|\.sn|\.so|\.sr|\.st|\.sv|\.sy|\.sz|\.tc|\.td|\.tf|'
                                     '\.tg|\.th|\.tj|\.tk|\.tl|\.tm|\.tn|\.to|\.tr|\.tt|\.tv|\.tw|\.tz|\.ua|\.ug|\.uk|'
                                     '\.us|\.uy|\.uz|\.va|\.vc|\.ve|\.vg|\.vi|\.vn|\.vu|\.wf|\.ws|\.ye|\.yt|\.yu|\.za|'
                                     '\.zm|\.zw|\.cs|\.eh|\.kp|\.ax|\.bv|\.gb|\.sj|\.um|\.tp|\.su|\.cs|\.dd|\.zr)'
                                     '((:\d{1,5})*)(?=(/|&|$)))'
                                     , url)

            if len(list_domain) == 0:
                print('[%s] No any domain, url: %s' % (self.feature_name, url))
            else:
                # print('[%s] has %d domain, url: %s' % (self.feature_name, len(list_domain), url))
                pass
            features.append(len(list_domain))

        return Series(features)
