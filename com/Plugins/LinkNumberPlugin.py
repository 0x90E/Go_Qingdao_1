#! /usr/bin/python
# -*- coding:utf-8 -*-

from pandas import Series
import tldextract
from com.Plugins.AbstractPlugin import AbstractPlugin
from com.Common.HttpRequest import *

class LinkNumberPlugin(AbstractPlugin):
    def __init__(self):
        AbstractPlugin.__init__(self, "link_number")

    def do_extract(self, simple_data):
        features = []
        for values in simple_data.values:
            outternal_link = 0

            split_url = tldextract.extract(parse_url(values[1]).netloc)
            domin_main = split_url.domain
            if split_url.suffix:
                domin_main += '.' + split_url.suffix
            soup = self.get_soup(values[0])
            if soup is None:
                features.append(0)
                continue

            # <link rel="stylesheet" href="mystyle.css">
            for tag_link in soup.findAll("link"):
                if not tag_link.has_attr("href"):
                    continue

                if not tag_link['href'].startswith("http"):
                    continue

                if domin_main not in tag_link['href']:
                    if "google.com" not in tag_link['href']:
                        outternal_link = outternal_link + 1

            # <script src="myscripts.js"></script>
            for tag_script in soup.findAll("script"):
                if not tag_script.has_attr("src"):
                    continue
                if not tag_script['src'].startswith("http"):
                    continue

                if domin_main not in tag_script['src']:
                    if "google.com" not in tag_script['src']:
                        outternal_link = outternal_link + 1

            # <meta name='syndication-source' content='https://mashable.com/2008/12/24/free-brand-monitoring-tools/'>
            for tag_meta in soup.findAll("meta"):
                if not tag_meta.has_attr("content"):
                    continue
                if not tag_meta['content'].startswith("http"):
                    continue

                if domin_main not in tag_meta['content']:
                    if "google.com" not in tag_meta['content']:
                        outternal_link = outternal_link + 1

            features.append(outternal_link)
            # total_link -> dark

        return Series(features)