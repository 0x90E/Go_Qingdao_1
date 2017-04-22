#! /usr/bin/python
# -*- coding:utf-8 -*-

import os
from abc import abstractmethod, ABCMeta
import chardet
from bs4 import BeautifulSoup


class AbstractPlugin:
    _metaclass__ = ABCMeta
    R_LEGITIMATE = '0'
    R_SUSPICIOUS = '1'
    R_PHISHING = '2'

    def __init__(self, feature_name):
        self.feature_name = feature_name

    @abstractmethod
    def do_extract(self, simple_data):
        """
            Retrieve data from the input source
            and return an feature series.
        """

    @abstractmethod
    def get_feature_name(self):
        """
            return the feature name.
        """
        return self.feature_name

    def get_soup(self, html_file):
        html_source = os.path.join("com/Files/test_data/file1/", html_file)
        # html_source = "/Users/Chung/GithubLocal/HTML_src_Attribute.html"
        if not os.path.exists(html_source):
            return None
        with open(html_source, 'rb') as f:
            input_bytes = f.read()
            result = chardet.detect(input_bytes)
            try:
                detected_unicode = input_bytes.decode(result['encoding'])
                soup = BeautifulSoup(detected_unicode)
                # print soup.prettify()       
            except (LookupError, UnicodeDecodeError, TypeError, RuntimeError):
                return None        
        return soup
