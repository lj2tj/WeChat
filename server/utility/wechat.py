#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import hashlib
from .httphelper import *
from .utilities import *
from .menu.menu import *
from ..constant import *


def check_signature(signature, timestamp, nonce):
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

def get_access_token():
    """
    Get access token, the access token will be refreshed every 1.5 hours.
    """
    global access_token
    global last_get_access_token_time
    global AppID
    global AppSecret

    if access_token:
        if datetime.datetime.now() < last_get_access_token_time + datetime.timedelta(hours=1.5):
            return access_token
    
    #Get new access_token
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (AppID, AppSecret)
    access_token_body = send_get_request(url)
    #set access_token
    access_token = get_json_value(access_token_body, "access_token")
    #set lat get access_token time
    last_get_access_token_time = datetime.datetime.now()

    # refresh menu
    create_menu()

    return access_token

def get_openID(request):
    """
    Get user OpenID from url or session.
	"""

	OpenID = request.GET("openid", None)

	if not OpenID:
		request.session.get("openid",default=None)
