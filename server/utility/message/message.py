#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET

def get_message_and_type(message):
    """
    @message: come from WeChat serevr.
    """
    tree = ET.fromstring(message)
    message_type = tree.find('MsgType').text
    return (tree, message_type)