#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from .utility.wechat import *
from .utility.utilities import *
from .utility.httphelper import *
from .utility.message.message import *
from .utility.message.message_generator import *
from .constant import *


########################################################################################
########################################  Entrance #####################################
########################################################################################
def create_menu():
    """
    Create WeChat menu by json file.
    """

    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % get_acceIss_token()
    jbody = load_menu_json()
    send_post_request(url, textmod=jbody)

@csrf_exempt
def wechat_home(request):
    # GET method represents that Wechat sent verification information
    if request.method == 'GET':
        # get signature, timestamp, nonce and echostr
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', 'error')
        # check_signature function tells whether the request is sent by wechat
        # not checked
        if not check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponse("Invalid signature")
        # checked
        else:
            response = echostr
            # refresh menu
            create_menu()
            return HttpResponse(response)
    elif request.method == 'POST':
        # POST method stands for Wechat sent user's messages
        # reply with our defined message
        content = ""
        data = request.read()
        xml,t = get_message_and_type(data)
        
        ToUserName = xml.find('ToUserName').text
        FromUserName = xml.find('FromUserName').text
        CreateTime = xml.find('CreateTime').text
        MsgId = xml.find('MsgId').text

        if t == "text":
            Content = xml.find('Content').text
            content = create_text_message(FromUserName, ToUserName, CreateTime, Content, MsgId)
        elif t == "image":
            PicUrl = xml.find('PicUrl').text
            MediaId = xml.find('MediaId').text
            content = create_image_message(FromUserName, ToUserName, CreateTime, PicUrl, MediaId, MsgId)
        elif t == "voice":
            MediaId = xml.find('MediaId').text
            Format = xml.find('Format').text
            content = create_voice_message(FromUserName, ToUserName, CreateTime, MediaId, Format, MsgId)
        elif t == "video":
            MediaId = xml.find('MediaId').text
            ThumbMediaId = xml.find('ThumbMediaId').text
            content = create_video_message(FromUserName, ToUserName, CreateTime, MediaId, ThumbMediaId, MsgId)
        elif t == "shortvideo":
            MediaId = xml.find('MediaId').text
            ThumbMediaId = xml.find('ThumbMediaId').text
            content = create_shortvideo_message(FromUserName, ToUserName, CreateTime, MediaId, ThumbMediaId, MsgId)
        elif t == "location":
            Location_X = xml.find('Location_X').text
            Location_Y = xml.find('Location_Y').text
            Scale = xml.find('Scale').text
            Label = xml.find('Label').text
            content = create_location_message(FromUserName, ToUserName, CreateTime, Location_X, Location_Y, Scale, Label, MsgId)
        elif t == "link":
            Title = xml.find('Title').text
            Description = xml.find('Description').text
            Url = xml.find('Url').text
            content = create_link_message(FromUserName, ToUserName, CreateTime, Title, Description, Url, MsgId)
        else:
            content = "Invalid message type"
        print(content)
        return HttpResponse(content)
    else:
        return HttpResponse("Unknown request type")

def index(request):
    key = "code"
    if request.method == "GET":
        state = request.GET.get('state', None)
        code = request.GET.get(key, None)
        if not code:
            code = request.session.get(key,default=None)
        if not code:
            return render(request, "index.html")
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code" % \
            (AppID, AppSecret, code)
        access_token_body = send_get_request(url)
        #set access_token
        access_token = get_json_value(access_token_body, "access_token")
        openid = get_json_value(access_token_body, "openid")
        return render(request, "index.html", context={"access_token":access_token, "openid":openid})
    else:
        return render(request, "index.html")