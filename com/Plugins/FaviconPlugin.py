#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
import tldextract
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class FaviconPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "favicon")

    def do_extract(self, simple_data):
        # Favicon Loaded From External Domain → Phishing; Otherwise → Legitimate
        features = []
        for values in simple_data.values:
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            split_url = tldextract.extract(parse_url(values[1]).netloc)
            domin_main = split_url.domain + "." + split_url.suffix
            is_phishing_website = False

            for tag_img in soup.findAll("img"):
                if not tag_img.has_attr("src"):
                    continue
                if not tag_img['src'].startswith("http"):
                    continue
                if "logo" in tag_img['src']:               
                    if domin_main not in tag_img['src']:
                        is_phishing_website = True
                    break

            if is_phishing_website:
                features.append(2)
                print "[Phishing] %s" %domin_main
            else:
                features.append(0)

        return Series(features)
