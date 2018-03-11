#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib
from urllib import request, parse
#import urllib2 

def send_get_request(url, header_dict=None):
    """
    @header_dict: {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    """
    with urllib.request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
    return data.decode('utf-8')

def _send_post_request(url, textmod, header_dict=None):
    """
    @header_dict: {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    @textmod: {"jsonrpc": "2.0","method":"user.login","params":{"user":"admin","password":"zabbix"},"auth": None,"id":1}
    """
    req = urllib.request.Request(url)
    if header_dict:
        for k,v in header_dict:
            req.add_header(k, v)
    
    with urllib.request.urlopen(req, data=textmod.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        return f.read().decode('utf-8')

"""
def send_post_request(url, textmod): 
    req = urllib2.Request(url) 
    data = urllib.urlencode(textmod) 
    #enable cookie 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
    response = opener.open(req, data) 
    return response.read() 
""" 
