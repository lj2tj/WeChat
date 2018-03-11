#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import hashlib
from .httphelper import *
from .utilities import *


class WeChatCMD():
    access_token = None
    last_get_access_token_time = datetime.datetime(2000, 1, 1)

    def __init__(self, AppID, AppSecret, token):
        
        #测试号
        self.AppID = AppID
        self.AppSecret = AppSecret
        self.token = token

    def check_signature(self, signature, timestamp, nonce):
        """
        Check if request sent from WeChat server.
        """

        if not signature:
            return False
        
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return True
        else:
            return False

    def get_access_token(self):
        """
        Get access token, the access token will be refreshed every 1.5 hours.
        """
        
        if WeChatCMD.access_token:
            if datetime.datetime.now() < WeChatCMD.last_get_access_token_time + datetime.timedelta(hours=1.5):
                return WeChatCMD.access_token
        
        #Get new access_token
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (self.AppID, self.AppSecret)
        access_token_body = send_get_request(url)
        #set access_token
        WeChatCMD.access_token = get_json_value(access_token_body, "access_token")

        #set lat get access_token time
        WeChatCMD.last_get_access_token_time = datetime.datetime.now()

        return WeChatCMD.access_token

    def get_openID(self, request):
        """
        Get user OpenID from url or session.
        """

        OpenID = request.GET("openid", None)

        if not OpenID:
            request.session.get("openid",default=None)
