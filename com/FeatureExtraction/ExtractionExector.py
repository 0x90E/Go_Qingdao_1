#! /usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
from pandas import DataFrame
from com.Plugins.AbstractPlugin import AbstractPlugin


class ExtractionExector():
    def __init__(self):
        self.plugin_list = []

    def do_extract(self, data_path, output_csv):
        sample_df = pd.read_csv(data_path, names=["top_url"])
        final_df = DataFrame(sample_df, copy=True)
        for plugin in self.plugin_list:
            print('doing %s' % plugin.get_feature_name())
            final_df[plugin.get_feature_name()] = plugin.do_extract(sample_df["top_url"])

        final_df.to_csv(output_csv, index=False)


    def register_plugin(self, plugin):
        if not isinstance(plugin, AbstractPlugin):
            print "Invalid plugin"
            return False

        if plugin not in self.plugin_list:
            self.plugin_list.append(plugin)

        return True