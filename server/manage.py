#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import os
import sys
import constant
from utility import wechat, httphelper, utilities
from utility.menu import menu
from utility.message import message, message_generator
from utility.user import user
from utility.persitent_media import persitent_media

def create_menu(accessToken):
    myMenu = menu.Menu()

    #Load Menu json file content
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "utility/menu", "menu.json")
    with open(json_path, 'r', encoding='utf-8') as f:
        postJson = f.read()
    
    print(type(postJson))
    result = myMenu.create(postJson, accessToken)
    print(result)

def get_media(accessToken, media_type):
    persitentMedia = persitent_media.PersitentMedia()
    medias = persitentMedia.batch_get(accessToken, mediaType=media_type)
    print("medias: ", medias)

if __name__ == "__main__":
    token = ""
    #测试号
    AppID = ""
    AppSecret = ""

    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        wechatCMD = wechat.WeChatCMD(AppID, AppSecret, token)
        accessToken = wechatCMD.get_access_token()

        if command == "create_menu":
            create_menu(accessToken)
        elif command == "get_media":
            get_media(accessToken, "image")