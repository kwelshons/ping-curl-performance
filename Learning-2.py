#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import pycurl
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, 'https://www.paloaltonetworks.com/')
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
