#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.Common.HttpRequest import *
from com.FeatureExtraction.ExtractionExector import ExtractionExector
from com.Plugins.ThinyUrlPlugin import ThinyUrlPlugin
from com.Plugins.DomainIpPlugin import DomainIpPlugin
from com.Plugins.Domain30dayPlugin import Domain30dayPlugin
from com.Plugins.DomainNumberPlugin import DomainNumberPlugin


if __name__ == "__main__":
    # set_proxy('127.0.0.1', 1080)
    print "Hello question one"
    extraction_exector = ExtractionExector()
    extraction_exector.register_plugin(ThinyUrlPlugin())
    extraction_exector.register_plugin(DomainIpPlugin())
    extraction_exector.register_plugin(Domain30dayPlugin())
    extraction_exector.register_plugin(DomainNumberPlugin())

    extraction_exector.do_extract("com/Files/cn_top1000.csv", "com/Files/output.csv",)
