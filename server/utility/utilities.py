#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def get_json_value(strJson, key):
	"""
	Get a property value in Json string.
	@key must by a property of json.
	"""
	j = json.loads(strJson)
	return j[key]
