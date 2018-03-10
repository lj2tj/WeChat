#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from ..httphelper import *
from ..wechat import *

def load_menu_json(json_path = None):
    """
    Load json file to create menu. if json_path is None, it will load default json file in same folder.
    The json file must be a valid WeChat menu json file.
    """

    if not json_path:
        json_path = "menu.json"
    
    with open(json_path, 'r') as f:
        menu_str = f.read()
    
    return menu_str

def create_menu():
    """
    Create WeChat menu by json file.
    """

    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % get_access_token()
    jbody = load_menu_json()
    send_post_request(url, textmod=jbody)
