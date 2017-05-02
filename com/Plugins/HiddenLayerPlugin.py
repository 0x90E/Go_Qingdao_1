#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *


class HiddenLayerPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "hidden_layer")

    def do_extract(self, simple_data):
        features = []
        count = 0

        for values in simple_data.values:
            count = count + 1
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            # <div style=”position: absolute; top: -999px;left: -999px;”>
            # 11ff3cb1360b3c657db844ce97bc3f7c
            is_find_feature = False
            for tag_div in soup.findAll("div"):
                if not tag_div.has_attr("style"):
                    continue
                else:
                    # print "tag_div[%s] %s" %(values[1], tag_div)
                    is_find_a_attr = False
                    for tmp in tag_div.recursiveChildGenerator():
                        if str(type(tmp)) == "<class 'bs4.element.Tag'>":
                            if tmp.name == "a":
                                is_find_a_attr = True
                                break

                    if not is_find_a_attr:
                        continue

                    if tag_div.has_attr("z-index"):
                        if int(tag_div["index"]) >= 999:
                            is_find_feature = True
                            features.append(1)
                            print "[hidden_layer][Dark][%s] %s" %(count, values[1])
                            break

            if not is_find_feature:
                features.append(0)

        return Series(features)
