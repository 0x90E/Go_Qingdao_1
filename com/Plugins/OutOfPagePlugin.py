#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class OutOfPagePlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "out_of_page")

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
                    is_find_a_attr = False
                    for tmp in tag_div.recursiveChildGenerator():
                        if str(type(tmp)) == "<class 'bs4.element.Tag'>":
                            if tmp.name == "a":
                                is_find_a_attr = True
                                break

                    if not is_find_a_attr:
                        continue

                    if "absolute" in tag_div["style"]:
                        # print "find style: %s %s" %(values[1], tag_div["style"])
                        is_find_nagtive_top = False
                        is_find_nagtive_left = False

                        for sub_str in tag_div["style"].split(";"):
                            if "left-" in sub_str:
                                continue
                            if "top-" in sub_str:
                                continue

                            if "top" in sub_str and "-" in sub_str and "px" in sub_str:
                                is_find_nagtive_top = True

                            if "left" in sub_str and "-" in sub_str and "px" in sub_str:
                                is_find_nagtive_left = True

                        if is_find_nagtive_top and is_find_nagtive_left:
                            print "[out_of_page][Dark][%s] %s %s" %(count, values[1], tag_div["style"])
                            features.append(1)
                            is_find_feature = True
                            break
            if not is_find_feature:
                features.append(0)

        return Series(features)
