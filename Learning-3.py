#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import click
import pycurl
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

buffer = BytesIO()
c = pycurl.Curl()

@click.command()
@click.option("-url", "--url", help="url list to ping", type=str,
              default="use text file")

def cli(url):
    """
    process a list of URLs and get pycurl results
    """

    if url == 'use text file':
        url_list = []
        with open('url_list.txt') as f:
            print('\nusing text file input\n')
            for line in f.readlines():
                url_list.append(line.rstrip())
    else:
        url_list = url.split(',')
        print('\n')

    for item in url_list:
        print(f'{item}')
        c.setopt(c.URL, f'{item}')
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()

#print('URL:' % c.URL)
# HTTP response code, expected 200.
print('HTTP response: %d' % c.getinfo(c.RESPONSE_CODE))
print('DNS Lookup Time: %f' % c.getinfo(c.NAMELOOKUP_TIME))
print('TCP Established Time: %f' % c.getinfo(c.CONNECT_TIME))
print('SSL Handshake Time: %f' % c.getinfo(c.APPCONNECT_TIME))
print('Pretransfer Time: %f' % c.getinfo(c.PRETRANSFER_TIME))
print('Redirect Time: %f' % c.getinfo(c.REDIRECT_TIME))
print('Time To First Byte: %f' % c.getinfo(c.STARTTRANSFER_TIME))
# Elapsed time for the transfer.
print('Total Time: %f' % c.getinfo(c.TOTAL_TIME))
print(f'\n')


c.close()
