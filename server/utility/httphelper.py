#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def send_get_request(url, header_dict=None):
	"""
	@header_dict: {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
	"""
	if header_dict:
		req = request.Request(url=url,headers=header_dict)
	else:
		req = request.Request(url=url)

	res = request.urlopen(req)
	res = res.read()
	return res.decode(encoding='utf-8')

def send_post_request(url, textmod, header_dict=None):
	"""
	@header_dict: {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
	@textmod: {"jsonrpc": "2.0","method":"user.login","params":{"user":"admin","password":"zabbix"},"auth": None,"id":1}
	"""
	textmod = json.dumps(textmod).encode(encoding='utf-8')
	if header_dict:
		req = request.Request(url=url,data=textmod,headers=header_dict)
	else:
		req = request.Request(url=url,data=textmod)
	res = request.urlopen(req)
	res = res.read()
	return res.decode(encoding='utf-8')
