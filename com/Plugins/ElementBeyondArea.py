#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class ElementBeyondArea(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "element_beyond_area")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            is_phishing_website = False
            try:
                for tag_form in soup.findAll():
                    if tag_form.has_attr("style"):
                        dst = tag_form["style"].lower().replace(' ', '')
                        if "top:-" in dst or "left:-" in dst:
                            print tag_form["style"]
                            is_phishing_website = True
                            break
                    elif tag_form.has_attr("Style"):
                        dst = tag_form["Style"].lower().replace(' ', '')
                        if "top:-" in dst or "left:-" in dst:
                            print tag_form["Style"]
                            is_phishing_website = True
                            break
                    else:
                        continue

            except Exception as e: # RuntimeError,
                print "RuntimeError!!"

            if is_phishing_website:
                features.append(1)
                print "[Phishing] %s" % values[1]
            else:
                features.append(0)
                print "[Normal] %s" % values[1]

        return Series(features)
