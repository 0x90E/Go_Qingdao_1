#! /usr/bin/python
# -*- coding:utf-8 -*-

import os
import pandas as pd
from pandas import DataFrame
from com.Plugins.AbstractPlugin import AbstractPlugin

URL_PLUGIN = "URL"
HTML_PLUGIN = "HTML"
MODE_TRAINING = "mode_training"
MODE_TESTING = "mode_TESTING"


class ExtractionExector():
    def __init__(self):
        self.url_plugin_list = []
        self.html_plugin_list = []

    def do_extract(self, mode, output_csv):
        if mode == MODE_TRAINING:
            data_path = "com/Files/subject1_sample/file_list.txt"
            name_list = ["id", "tag", "file_name", "url"]
        elif mode == MODE_TESTING:
            data_path = "com/Files/subject1_A/file_list.txt"
            name_list = ["id", "file_name", "url"]

        sample_df = pd.read_csv(data_path, names=name_list)
        final_df = DataFrame(sample_df, copy=True)
        len_input_data = len(final_df.index)
        for plugin in set(self.url_plugin_list):
            print('[URL]doing %s' % plugin.get_feature_name())
            tmp_features = plugin.do_extract(sample_df["url"])
            if len(tmp_features.index) != len_input_data:
                print "len of tmp_features.index: %s: " %tmp_features.index
                print "len of input_data: %s: " %len_input_data
            assert len(tmp_features.index) == len_input_data
            final_df[plugin.get_feature_name()] = tmp_features
        for plugin in set(self.html_plugin_list):
            print('[HTML]doing %s' % plugin.get_feature_name())
            plugin.set_html_dir(os.path.join(os.path.dirname(data_path), "file"))
            tmp_features = plugin.do_extract(sample_df[["file_name", "url"]])
            if len(tmp_features.index) != len_input_data:
                print "len of tmp_features.index: %s: " %tmp_features.index
                print "len of input_data: %s: " %len_input_data            
            assert len(tmp_features.index) == len_input_data
            final_df[plugin.get_feature_name()] = tmp_features
            

        final_df.to_csv(output_csv, index=False)


    def register_plugin(self, plugin_class, plugin):
        if not isinstance(plugin, AbstractPlugin):
            print "Invalid plugin"
            return False


        if plugin_class == URL_PLUGIN:
            self.url_plugin_list.append(plugin)
        elif plugin_class == HTML_PLUGIN:
            self.html_plugin_list.append(plugin)
        else:
            return False

        return True