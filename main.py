#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.FeatureExtraction.ExtractionExector import ExtractionExector
from com.Plugins.ThinyUrlPlugin import ThinyUrlPlugin

if __name__ == "__main__":
    print "Hello question one"
    extraction_exector = ExtractionExector()
    extraction_exector.register_plugin(ThinyUrlPlugin())

    extraction_exector.do_extract("com/Files/cn_top100.csv", "com/Files/output.csv",)
