#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json

def get_json_value(strJson, key):
    """
    Get a property value in Json string.
    @key must by a property of json.
    """
    j = json.loads(strJson)
    k = j.get(key, None)
    return k
