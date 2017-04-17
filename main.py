#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.Common.HttpRequest import *
from com.FeatureExtraction.ExtractionExector import ExtractionExector
from com.Plugins.ThinyUrlPlugin import ThinyUrlPlugin
from com.Plugins.DomainIpPlugin import DomainIpPlugin
from com.Plugins.Domain30dayPlugin import Domain30dayPlugin
from com.Plugins.DomainNumberPlugin import DomainNumberPlugin
from com.Plugins.DomainSubNumberPlugin import DomainSubNumberPlugin
from com.Plugins.UrlLongPlugin import UrlLongPlugin
from com.Plugins.DomainMultiSubPlugin import DomainMultiSubPlugin
from com.Plugins.DomainWithHttpsPlugin import DomainWithHttpsPlugin
from com.Plugins.DomainPortOtherPlugin import DomainPortOtherPlugin
from com.Plugins.UrlPathDepthPlugin import UrlPathDepthPlugin
from com.Plugins.DomainFakePayPlugin import DomainFakePayPlugin
from com.Common.ChinazQuery import ChinazQuery

if __name__ == "__main__":
    # set_proxy('127.0.0.1', 1080)
    print "Hello question one"

    extraction_exector = ExtractionExector()
    extraction_exector.register_plugin(ThinyUrlPlugin())
    extraction_exector.register_plugin(DomainIpPlugin())
    extraction_exector.register_plugin(Domain30dayPlugin())
    extraction_exector.register_plugin(DomainNumberPlugin())
    extraction_exector.register_plugin(DomainSubNumberPlugin())
    extraction_exector.register_plugin(UrlLongPlugin())
    # extraction_exector.register_plugin(DomainMultiSubPlugin())
    # extraction_exector.register_plugin(DomainWithHttpsPlugin())
    # extraction_exector.register_plugin(DomainPortOtherPlugin())
    # extraction_exector.register_plugin(UrlPathDepthPlugin())
    extraction_exector.register_plugin(DomainFakePayPlugin())
    extraction_exector.do_extract("com/Files/url.csv", "com/Files/output.csv",)

