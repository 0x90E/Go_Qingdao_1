import urllib2
import socks
import socket
import urlparse
from com.Common.Other import *

def read_html(url):
    content = read_cache(url)
    if content:
        return content
    try:
        data = urllib2.urlopen(url)
        content = data.read()
        write_cache(url, content)
        return content
    except Exception, e:
        return None


def parse_url(url):
    if url[:7] != 'http://' and url[:8] != 'https://':
        url = 'http://' + url
    try:
        return urlparse.urlparse(url)
    except:
        return None


def set_proxy(host, port):
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, host, port)
    socket.socket = socks.socksocket
