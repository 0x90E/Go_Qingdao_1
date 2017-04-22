#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
import tldextract
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class IFrameToOtherDomain(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "iframe_to_other_domain")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            split_url = tldextract.extract(parse_url(values[1]).netloc)
            domin_main = split_url.domain + "." + split_url.suffix
            is_phishing_website = False

            try:
                for tag_iframe in soup.findAll("iframe"):
                    if not tag_iframe.has_attr("src"):
                        continue
                    if not tag_iframe['src'].startswith("http"):
                        continue           
                    if domin_main not in tag_iframe['src']:
                        is_phishing_website = True
                        break

                if is_phishing_website:
                    features.append(2)
                    print "[Phishing] %s" %domin_main
                else:
                    features.append(0)

            except RuntimeError:
                print "RuntimeError!!"
                features.append(0)

        return Series(features)
