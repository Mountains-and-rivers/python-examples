#!/usr/bin/env python3
# coding: utf-8

"""查看本机IP."""

import socket

import requests
import socks
from lxml import etree


def main():
    headers_html = {
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    # 使用 socks5 方法 1，使用全局 socks5 代理
    # socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 1080)
    # socket.socket = socks.socksocket
    url = 'https://www.ipip.net/ip.html'
    with requests.Session() as session:
        session.headers.update(headers_html)
        # 使用 socks5 方法 2，局部
        session.proxies = {
            'http': 'socks5://127.0.0.1:1080',
            'https': 'socks5://127.0.0.1:1080'
        }
        r = session.get(url)
        selector = etree.HTML(r.text)
        ip = selector.xpath('.//form[@method="post"]/input[@name="ip"]/@value')[0]
        print(ip)


if __name__ == '__main__':
    main()
