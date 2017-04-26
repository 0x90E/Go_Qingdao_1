#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
import tldextract
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class UrlOfAnchorPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "url_of_anchor")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            suspicious_href = 0
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            split_url = tldextract.extract(parse_url(values[1]).netloc)
            domin_main = split_url.domain
            if split_url.suffix:
                domin_main += '.' + split_url.suffix

            for tag_a in soup.findAll("a"):
                if not tag_a.has_attr("href"):
                    continue
                href_attr = tag_a["href"]
                if href_attr.startswith("#"):
                    suspicious_href = suspicious_href + 1
                elif href_attr.startswith("javascript"):
                    suspicious_href = suspicious_href + 1
                elif href_attr.startswith("http"):
                    if domin_main not in href_attr:
                        suspicious_href = suspicious_href + 1

            features.append(suspicious_href)

        return Series(features)
