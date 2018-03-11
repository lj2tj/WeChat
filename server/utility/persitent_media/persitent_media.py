#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib
import json
import datetime

class PersitentMedia(object):
    def __init__(self):
        pass
    
    #上传图文
    def add_news(self, accessToken, news):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(postUrl, news)
        return urlResp.read()
    
    """
    #上传
    def uplaod(self, accessToken, filePath, mediaType):
        openFile = open(filePath, "rb")
        fileName = "hello"
        param = {'media': openFile, 'filename': fileName}
        #param = {'media': openFile}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=%s" % (accessToken, mediaType)
        request = urllib2.Request(postUrl, postData, postHeaders)
        urlResp = urllib2.urlopen(request)
        print urlResp.read()

    """

    #下载
    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/get_material?access_token=%s" % accessToken
        postData = { "media_id": mediaId }
        urlResp = urllib.request.urlopen(postUrl, postData)
        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print(jsonDict)
        else:
            d = datetime.datetime.now()
            buffer = urlResp.read()  # 素材的二进制
            mediaFile = file(str(d)+".jpg", "wb")
            mediaFile.write(buffer)
            print("get successful: " + str(d)+".jpg")

    #删除
    def delete(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/del_material?access_token=%s" % accessToken
        postData = { "media_id": mediaId } 
        urlResp = urllib.request.urlopen(postUrl, postData)
        return urlResp.read()

    #获取素材列表
    def batch_get(self, accessToken, mediaType, offset=0, count=20):
        """
        @mediaType: 素材的类型，图片（image）、视频（video）、语音 （voice）、图文（news）
        @offset: 从全部素材的该偏移位置开始返回，0表示从第一个素材 返回
        @count: 返回素材的数量，取值在1到20之间
        """
        
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s" % accessToken
        postData = '''{ 
            "type": "%s", 
            "offset": %s, 
            "count": %s 
        }''' % (mediaType, offset, count)

        urlResp = urllib.request.urlopen(url=postUrl, data=postData.encode(encoding='UTF8')) 
        return urlResp.read()
