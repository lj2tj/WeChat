#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from ..wechat import *

def update_user_remark(openid, remark_name):
    """
    Update user remark name.
    """
    url = "https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token=%s" % get_access_token()
    jbody = {
        "openid":openid,
        "remark":remark_name
    }
    result = send_post_request(url, textmod=jbody)

