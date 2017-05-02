#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin

class DisablingRightClickPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "disabling_right_click")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue   

            try:
                # document.addEventListener('contextmenu', event => event.preventDefault());
                if "contextmenu" in soup.prettify() and "preventDefault" in soup.prettify():
                    features.append(1)
                    print "[right_click][Phishing] %s" %values[1]
                    continue

                # event.button==2
                if "event.button" in soup.prettify() and "2" in soup.prettify():
                    features.append(1)
                    print "[right_click][Phishing] %s" %values[1]
                    continue

                features.append(0)

            except RuntimeError:
                print "RuntimeError!!"
                features.append(0)          

        return Series(features)        
