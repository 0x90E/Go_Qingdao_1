#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.Common.HttpRequest import *
from com.FeatureExtraction.ExtractionExector import *
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
from com.Plugins.FaviconPlugin import FaviconPlugin
from com.Plugins.RequestUrlPlugin import RequestUrlPlugin
from com.Plugins.UrlOfAnchorPlugin import UrlOfAnchorPlugin
from com.Plugins.LinkNumberPlugin import LinkNumberPlugin
from com.Plugins.SubmittingToEmailPlugin import SubmittingToEmailPlugin
from com.Plugins.DisablingRightClickPlugin import DisablingRightClickPlugin
from com.Plugins.IFrameRedirectionPlugin import IFrameRedirectionPlugin
from com.Plugins.HiddenNumberPlugin import HiddenNumberPlugin
from com.Plugins.IFrameToOtherDomain import IFrameToOtherDomain
from com.Plugins.IcpPlugin import IcpPlugin
from com.Plugins.HyperlinkColorWhite import HyperlinkColorWhite
from com.Plugins.HyperlinkSizeSmall import HyperlinkSizeSmall
from com.Plugins.ElementHide import ElementHide
from com.Plugins.HrefHide1 import HrefHide1
from com.Plugins.HrefHide2 import HrefHide2
from com.Plugins.HrefHide3 import HrefHide3
from com.Plugins.ElementBeyondArea import ElementBeyondArea
from com.Plugins.OutOfPagePlugin import OutOfPagePlugin
from com.Plugins.MarqueeNumberPlugin import MarqueeNumberPlugin
from com.Plugins.MarqueeNumberJsPlugin import MarqueeNumberJsPlugin
from com.Plugins.HiddenLayerPlugin import HiddenLayerPlugin
from com.Plugins.KeywordOfA import KeywordOfA
from com.Plugins.UrlIncludeAspPlugin import UrlIncludeAspPlugin
from com.Common.HttpRequest import *


def question_dark_website():
    extraction_exector = ExtractionExector()
    extraction_exector.register_plugin(HTML_PLUGIN, HyperlinkColorWhite())
    extraction_exector.register_plugin(HTML_PLUGIN, HyperlinkSizeSmall())
    extraction_exector.register_plugin(HTML_PLUGIN, ElementHide())
    extraction_exector.register_plugin(HTML_PLUGIN, HrefHide1())
    extraction_exector.register_plugin(HTML_PLUGIN, HrefHide2())
    extraction_exector.register_plugin(HTML_PLUGIN, HrefHide3())
    extraction_exector.register_plugin(HTML_PLUGIN, ElementBeyondArea())    
    # extraction_exector.register_plugin(HTML_PLUGIN, OutOfPagePlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, MarqueeNumberPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, MarqueeNumberJsPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, KeywordOfA())
    extraction_exector.register_plugin(URL_PLUGIN, UrlIncludeAspPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, LinkNumberPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, IFrameToOtherDomain())
    extraction_exector.do_extract(MODE_TRAINING, "com/Files/output_TRAINING_dark_website.csv")

def question_phishing_website():
    extraction_exector = ExtractionExector()
    extraction_exector.register_plugin(URL_PLUGIN, ThinyUrlPlugin())
    extraction_exector.register_plugin(URL_PLUGIN, DomainIpPlugin())
    # extraction_exector.register_plugin(URL_PLUGIN, Domain30dayPlugin())
    extraction_exector.register_plugin(URL_PLUGIN, DomainNumberPlugin())
    extraction_exector.register_plugin(URL_PLUGIN, DomainSubNumberPlugin())
    extraction_exector.register_plugin(URL_PLUGIN, UrlLongPlugin())
    extraction_exector.register_plugin(URL_PLUGIN, DomainMultiSubPlugin())
    extraction_exector.register_plugin(URL_PLUGIN, DomainWithHttpsPlugin())
    extraction_exector.register_plugin(URL_PLUGIN, DomainPortOtherPlugin())
    extraction_exector.register_plugin(URL_PLUGIN, UrlPathDepthPlugin())
    extraction_exector.register_plugin(URL_PLUGIN, DomainFakePayPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, RequestUrlPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, UrlOfAnchorPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, DisablingRightClickPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, LinkNumberPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, SubmittingToEmailPlugin())
    extraction_exector.register_plugin(HTML_PLUGIN, IFrameToOtherDomain())
    extraction_exector.register_plugin(HTML_PLUGIN, IFrameRedirectionPlugin())
    # extraction_exector.register_plugin(HTML_PLUGIN, IcpPlugin())

    # MODE_TRAINING, MODE_TESTING
    extraction_exector.do_extract(MODE_TRAINING, "com/Files/output_TRAINING.csv")    

if __name__ == "__main__":
    print "Hello question one"
    # question_phishing_website()
    question_dark_website()

