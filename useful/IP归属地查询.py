#!/usr/bin/env python3
# coding: utf-8

"""IP归属地查询."""

from urllib import request

from lxml import etree


def get_html(ip):
    url = f'http://m.ip138.com/ip.asp?ip={ip}'
    with request.urlopen(url) as response:
        return response.read()


def parse_html(html):
    s = etree.HTML(html)
    addr_info = s.xpath('//p[@class="result"]/text()')
    for n in addr_info:
        print(n)


def main():
    ip = '192.168.1.1'
    html = get_html(ip)
    parse_html(html)


if __name__ == '__main__':
    main()
