#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class MarqueeNumberPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "marquee_number")

    def do_extract(self, simple_data):
        features = []
        count = 0
        for values in simple_data.values:
            count = count + 1
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            is_find_feature = False
            for tag_marquee in soup.findAll("marquee"):
                is_find_a_attr = False
                for tmp in tag_marquee.recursiveChildGenerator():
                    if str(type(tmp)) == "<class 'bs4.element.Tag'>":
                        if tmp.name == "a":
                            is_find_a_attr = True
                            break

                if not is_find_a_attr:
                    # features.append(0)
                    # break    # error, will be detect the first marquee
                    continue

                if tag_marquee.has_attr("height"):
                    if tag_marquee["height"] == "1":
                        is_find_feature = True
                        features.append(1)
                        print "[marquee_number][Dark][%s] %s" %(count, values[1])
                        break

                if tag_marquee.has_attr("width"):
                    if tag_marquee["width"] == "1":
                        is_find_feature = True
                        features.append(1)
                        print "[marquee_number][Dark][%s] %s" %(count, values[1])
                        break

            if not is_find_feature:
                features.append(0)

        return Series(features)

# <marquee height=1 width=5 scrollamount=3000 scrolldelay=20000> <a> </marquee> marquee的height or width 其中一个为1
