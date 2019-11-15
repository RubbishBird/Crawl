#-*-coding:utf-8-*-

'''
单线程实现
'''

import requests
from lxml import etree
import threading
import os
from urllib import request
import re

save_path = 'D:/photos/doutu/'

def show_percent(a,b,c):
    '''回调函数
        @a:已经下载的数据块
        @b:数据块的大小
        @c:远程文件的大小
        '''
    per = 100.0*a*b/c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


def parse_url(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        name = img.get('alt')
        # 将name中的特殊字符用空格替换掉
        name =re.sub(r'[\.。？\?!！]','',name)
        suffix =os.path.splitext(img_url)[1]
        img_name = name + suffix
        print(img_name)
        #判断文件是否存在，如果不存在则进行下载
        if not os.path.isfile(os.path.join(save_path, img_name)):
            request.urlretrieve(img_url,filename=save_path + img_name,reporthook=show_percent)
        else:
            print("图片已经存在！")



def main():
    for x in range(1,5):
        url = 'http://www.doutula.com/photo/list/?page=%d'% x
        parse_url(url)


if __name__ == '__main__':
    main()