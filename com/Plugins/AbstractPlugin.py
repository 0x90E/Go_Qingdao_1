#! /usr/bin/python
# -*- coding:utf-8 -*-

from abc import abstractmethod, ABCMeta


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
