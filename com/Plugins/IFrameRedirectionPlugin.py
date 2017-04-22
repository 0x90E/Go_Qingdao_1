#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
import tldextract
from com.Plugins.AbstractPlugin import AbstractPlugin


class IFrameRedirectionPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "iframe_redirection")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue   

            try:
                # <iframe src="https://jshao.haolepic.com/haoxxoo.html" frameborder="0"
                for tag_iframe in soup.findAll("iframe"):
                    if not tag_iframe.has_attr("frameborder"):
                        continue
                    print "[Phishing] %s" %values[1]
                    features.append(2)
                    break
            except RuntimeError:
                print "RuntimeError!!"
                features.append(0)       

        return Series(features)        
