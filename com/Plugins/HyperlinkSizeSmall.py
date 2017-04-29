#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class HyperlinkSizeSmall(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "hyperlink_size_small")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            is_phishing_website = False
            try:
                for tag_form in soup.findAll("a"):
                    if not tag_form.has_attr("style"):
                        continue
                    if (":1px" in tag_form["style"].lower()) or \
                            (":0px" in tag_form["style"].lower()):
                        is_phishing_website = True
                        break
            except RuntimeError:
                print "RuntimeError!!"

            if is_phishing_website:
                features.append(1)
                print "[Phishing] %s" % values[1]
            else:
                features.append(0)
                print "[Normal] %s" % values[1]

        return Series(features)
