#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class KeywordOfA(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "keyword_of_a")
        self.keyword_list = [u"博彩", u"赌场", u"威尼斯人", u"娱乐场", u"投注", u"六合彩",
                             u"娱乐城", u"百家乐", u"医疗", u"减肥", u"外挂", u"彩铃",\
                             u"新葡京", u"赌博", u" hg0088", u"皇冠"]

    def do_extract(self, simple_data):
        features = []
        count = 0
        for values in simple_data.values:
            count = count + 1
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            keyword_count = 0
            for tag_a in soup.findAll("a"):
                if not tag_a.has_attr("href"):
                    continue
                # print "text: %s" %tag_a.get_text()
                for keyword in self.keyword_list:
                    tmp_count = tag_a.get_text().count(keyword)
                    if tmp_count > 0:
                        keyword_count = keyword_count + tmp_count
                        break

            print "[keyword_of_a][%s]%s %s" %(count, values[1], keyword_count)
            features.append(keyword_count)

        return Series(features)
