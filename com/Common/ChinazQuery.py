#! /usr/bin/python
# -*- coding:utf-8 -*-

import httplib
from bs4 import BeautifulSoup

# https://www.anquan.org/
# http://icp.chinaz.com

class ChinazQuery:
    def __init__(self):
        self.soup = None

    def get_website_basic_info(self, target_url):
        method_list = []
        method_list.append(self._get_backward_link)
        method_list.append(self._get_backward_link)
        method_list.append(self._get_record_date)
        method_list.append(self._get_website_introduction)
        method_list.append(self._get_access_speed)
        method_list.append(self._get_origin)
        method_list.append(self._get_dir_categorization)
        method_list.append(self._get_adult_content)
        self._do_query("alexa.chinaz.com", target_url, method_list)

    def get_whois_info(self, target_url):
        method_list = []
        self._do_query("whois.chinaz.com", target_url, method_list)

    def _do_query(self, chinaz_website, target_url, method_list):
        conn = httplib.HTTPConnection(chinaz_website)
        conn.request("GET", "/" + target_url)
        res = conn.getresponse()
        if res.status != 200:
            return 
        data = res.read()
        self.soup = BeautifulSoup(data)
        # print(self.soup.prettify())
        
        for method in method_list:
            method()

    def _get_global_rank(self):
        for tag_h4 in self.soup.find_all('h4'):
            if u"网站" in tag_h4:
                if u"没有全球综合排名" in tag_h4.get_text():
                    return 0
                else:
                    tag_ems = tag_h4.find_all('em')
                    return int(tag_ems[1].get_text() )
                break

    def _get_backward_link(self):
        self._get_website_info(u"反向链接")

    def _get_record_date(self):
        self._get_website_info(u"收录日期")
        # 没有记录

    def _get_website_introduction(self):
        self._get_website_info(u"网站简介")
        # 该站点还没有向ALEXA提交任何介绍信息。

    def _get_dir_categorization(self):
        self._get_website_info(u"所属目录")
        # 该站未被亚马逊分类目录收录

    def _get_access_speed(self):
        self._get_website_info(u"访问速度")
        # 没有记录 

    def _get_origin(self):
        self._get_website_info(u"所属国家")
        # 不详

    def _get_adult_content(self):
        self._get_website_info(u"成人内容")
        # 没有记录
        # NO -> 正常

    def _get_website_info(self, keyword):
        for tag_ul in self.soup.find_all('ul'):
            if not tag_ul.has_attr("class"):
                continue
            if "info_detail" in tag_ul["class"]:
                for tag_li in tag_ul.find_all('li'):
                    for tag_span in tag_li.findChildren("span"):
                        if keyword in tag_span.get_text():
                            return tag_li.get_text().split(u"：")[1]
