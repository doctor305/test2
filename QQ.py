# -*- coding:utf-8 -*-

import json
import urllib2
import os

album1 = "http://alist.photo.qq.com/"
album2 = "http://xalist.photo.qq.com/"

albumbase1 = "http://alist.photo.qq.com/fcgi-bin/fcg_list_album?uin="#如果没有设置密保的相册是通过这个地址访问的
albumbase2 = "http://xalist.photo.qq.com/fcgi-bin/fcg_list_album?uin="#//设置密保的相册是通过这个地址访问的

photo1 = "http://plist.photo.qq.com/"
photo2 = "http://xaplist.photo.qq.com/"
photobase1 = "http://plist.photo.qq.com/fcgi-bin/fcg_list_photo?uin="
photobase2 = "http://xaplist.photo.qq.com/fcgi-bin/fcg_list_photo?uin="
##savepath = ''
class Album:
    def __init__(self, uid, name, count):
        self.ID = uid
        self.Name = name
        self.Count = count


class Photo:
    def __init__(self, url, name, album):
        self.URL = url
        self.Name = name
        self.Album = album
def getAblums(qq, url):
    ablums = list()
    print url + qq + "&outstyle=2"
    request = urllib2.Request(url + qq + "&outstyle=2")
    f = urllib2.urlopen(request, timeout=10)
    response = f.read().decode('gbk')
    f.close()
    response = response.replace('_Callback(', '')
    response = response.replace(');', '')
##    print response
##    print json.loads(response)
    if 'album' in json.loads(response):
        for i in json.loads(response)['album']:
            ablums.append(Album(i['id'], i['name'], i['total']))
    return ablums


def getPhotosByAlum(album, qq, url):
    photos = list()
    print url + qq + "&albumid=" + album.ID + "&outstyle=json"
    request = urllib2.Request(url + qq + "&albumid=" + album.ID + "&outstyle=json")
    f = urllib2.urlopen(request, timeout=10)
    response = f.read().decode('gbk')
    f.close()
    response = response.replace('_Callback(', '')
    response = response.replace(');', '')
    #print response
    if 'pic' in json.loads(response):
        for i in json.loads(response)['pic']:
            photos.append(Photo(i['url'], i['name'], album))
    return photos


def saveImage( photo, qq, index):
    print index, photo.URL
    url = photo.URL.replace('\\', '')
    f = urllib2.urlopen(url, timeout=10)
    data = f.read()
    f.close()
    if not os.path.exists(qq):
        os.mkdir(qq)
    with open(qq +os.path.sep+ index + '.jpeg', "wb") as code:
        code.write(data)
        code.close()


def savePhotos(qq):
    print u'获取：'+qq+u'的相册信息'
    ablums = getAblums(qq, albumbase2)
##    ablums = getAblums(qq, albumbase1)
    if len(ablums) > 0:
        for i, a in enumerate(ablums):
            if a.Count > 0:
                print u'开始下载第'+str(i+1)+u'个相册'
                photos = getPhotosByAlum(a, qq, photobase2)
##                photos = getPhotosByAlum(a, qq, photobase1)
                for index, p in enumerate(photos):
                    saveImage( p, qq, str(i)+'_'+str(index))
                print u'第'+str(i+1)+u'个相册下载完成'
    else:
        print u'读取到得相册个数为0'

if __name__ == "__main__":
    while True:
        try:
            print u'请输入需要下载的QQ号码(输入0退出)： '
            qq = int(raw_input())
            if qq == 0:
                break
            savePhotos(str(qq))

            print
            print u'下载完毕！'
            print

        except:
            print u'输入的QQ号码有误！'
        
    
