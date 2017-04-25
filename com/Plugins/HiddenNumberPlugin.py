#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin

class HiddenNumberPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "hidden_number")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            # soup = self.get_soup(values[0])
            soup = self.get_soup("0e51114c74c8e5a9a0c3d651fcf49307")
            if soup is None:
                features.append(0)
                continue   

            try:
                # ./0e51114c74c8e5a9a0c3d651fcf49307
                for tag_hidden in soup.findAll("hidden"):
                    print "got hidde: %s" %tag_hidden
                    # print "[Phishing] %s" %values[1]
                    features.append(2)
                    break

                features.append(0)

            except RuntimeError:
                print "RuntimeError!!"
                features.append(0)
            break

        return Series(features)        