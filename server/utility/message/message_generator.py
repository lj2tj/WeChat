#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def create_text_message(ToUserName, FromUserName, CreateTime, Content, MsgId):
    x = """<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName> 
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    <MsgId>%s</MsgId>
</xml>""" % (ToUserName, FromUserName, CreateTime, Content, MsgId)
    return x

def create_image_message(ToUserName, FromUserName, CreateTime, PicUrl, MediaId, MsgId):
    x = """<xml> 
    <ToUserName><![CDATA[%s]]></ToUserName> 
    <FromUserName><![CDATA[%s]]></FromUserName> 
    <CreateTime>%s</CreateTime> 
    <MsgType><![CDATA[image]]></MsgType> 
    <PicUrl><![CDATA[%s]]></PicUrl> 
    <MediaId><![CDATA[%s]]></MediaId> 
    <MsgId>%s</MsgId> 
</xml>""" % (ToUserName, FromUserName, CreateTime, PicUrl, MediaId, MsgId)
    return x

def create_voice_message(ToUserName, FromUserName, CreateTime, MediaId, Format, MsgId):
    x = """<xml>
    <ToUserName><![CDATA[%s]]></ToUserName> 
    <FromUserName><![CDATA[%s]]></FromUserName> 
    <CreateTime>%s</CreateTime> 
    <MsgType><![CDATA[voice]]></MsgType>
    <MediaId><![CDATA[%s]]></MediaId>
    <Format><![CDATA[%s]]></Format>
    <MsgId>%s</MsgId>
</xml>""" % (ToUserName, FromUserName, CreateTime, MediaId, Format, MsgId)
    return x

def create_video_message(ToUserName, FromUserName, CreateTime, MediaId, ThumbMediaId, MsgId):
    x = """<xml>
    <ToUserName><![CDATA[%s]]></ToUserName> 
    <FromUserName><![CDATA[%s]]></FromUserName> 
    <CreateTime>%s</CreateTime> 
    <MsgType><![CDATA[video]]></MsgType>
    <MediaId><![CDATA[%s]]></MediaId>
    <ThumbMediaId><![CDATA[%s]]></ThumbMediaId>
    <MsgId>%s</MsgId>
</xml>""" % (ToUserName, FromUserName, CreateTime, MediaId, ThumbMediaId, MsgId)
    return x

def create_shortvideo_message(ToUserName, FromUserName, CreateTime, MediaId, ThumbMediaId, MsgId):
    x = """<xml>
    <ToUserName><![CDATA[%s]]></ToUserName> 
    <FromUserName><![CDATA[%s]]></FromUserName> 
    <CreateTime>%s</CreateTime> 
    <MsgType><![CDATA[shortvideo]]></MsgType>
    <MediaId><![CDATA[%s]]></MediaId>
    <ThumbMediaId><![CDATA[%s]]></ThumbMediaId>
    <MsgId>%s</MsgId>
</xml>""" % (ToUserName, FromUserName, CreateTime, MediaId, ThumbMediaId, MsgId)
    return x

def create_location_message(ToUserName, FromUserName, CreateTime, Location_X, Location_Y, Scale, Label, MsgId):
    x = """<xml>
    <ToUserName><![CDATA[%s]]></ToUserName> 
    <FromUserName><![CDATA[%s]]></FromUserName> 
    <CreateTime>%s</CreateTime> 
    <MsgType><![CDATA[location]]></MsgType>
    <Location_X>%s</Location_X>
    <Location_Y>%s</Location_Y>
    <Scale>%s</Scale>
    <Label><![CDATA[%s]]></Label>
    <MsgId>%s</MsgId>
</xml>""" % (ToUserName, FromUserName, CreateTime, Location_X, Location_Y, Scale, Label, MsgId)
    return x

def create_link_message(ToUserName, FromUserName, CreateTime, Title, Description, Url, MsgId):
    x = """<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[link]]></MsgType>
    <Title><![CDATA[%s]]></Title>
    <Description><![CDATA[%s]]></Description>
    <Url><![CDATA[%s]]></Url>
    <MsgId>%s</MsgId>
</xml>""" % (ToUserName, FromUserName, CreateTime, Title, Description, Url, MsgId)
    return x