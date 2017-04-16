import urllib2
import hashlib
import socks
import socket
import urlparse


def md5(content):
    m1 = hashlib.md5()
    m1.update(content)
    return m1.hexdigest()


def read_cache(url):
    file_name = md5(url)
    try:
        file = open('com/Files/cache/%s' % file_name, 'r')
        data = file.read()
        file.close()
        return data
    except:
        return None


def write_cache(url, content):
    file_name = md5(url)
    try:
        file = open('com/Files/cache/%s' % file_name, 'w+')
        file.write(content)
        file.close()
        return True
    except:
        return False


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
