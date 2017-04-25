#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
import tldextract
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class RequestUrlPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "request_url")

    def do_extract(self, simple_data):
        # within a webpage such as images, videos and sounds are loaded from another domain
        used_src_elements = ["audio", "embed", "iframe", "img", "input", "script",
                             "input", "script", "source", "video", "track"]
        features = []
        for values in simple_data.values:
            total_src = 0.0
            outternal_src = 0.0
            
            split_url = tldextract.extract(parse_url(values[1]).netloc)
            domin_main = split_url.domain
            if split_url.suffix:
                domin_main += '.' + split_url.suffix
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue
                        
            for element in used_src_elements:
                for tag in soup.findAll(element):
                    if not tag.has_attr("src"):
                        continue

                    total_src = total_src + 1
                    if not tag['src'].startswith("http"):
                        continue

                    if domin_main not in tag['src']:
                        if "google.com" not in tag['src']:
                            outternal_src = outternal_src + 1

                    # "track" is sub tag of video or audio
                    if element in ["audio", "video"]:
                        for track_tag in tag.findAll("track"):
                            if not track_tag.has_attr("src"):
                                continue

                            total_src = total_src + 1
                            if not track_tag['src'].startswith("http"):
                                continue

                            if domin_main not in track_tag['src']:
                                outternal_src = outternal_src + 1
            
            if total_src == 0:
                features.append(0)
            elif (outternal_src/total_src) <= 0.22:
                features.append(0)
            elif (outternal_src/total_src) >= 0.22 and (outternal_src/total_src) < 0.61:
                features.append(1)
                print "[Suspicious]score :%s %s" %(outternal_src/total_src, domin_main)
            else:
                features.append(2)
                print "[Phishing]score :%s %s" %(outternal_src/total_src, domin_main)

        return Series(features)
