#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

def load_menu_json():
    """
    Load json file to create menu. if json_path is None, it will load default json file in same folder.
    The json file must be a valid WeChat menu json file.
    """
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "menu.json")
    with open(json_path, 'r', encoding='utf-8') as f:
        menu_str = f.read()
    
    return menu_str
