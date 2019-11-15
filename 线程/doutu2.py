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
from queue import Queue

save_path = 'D:/photos/doutu/'


class Procuder(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Procuder, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_url(url)

    def parse_url(self,url):
        response = requests.get(url, headers=self.headers)
        text = response.text
        print(text)
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            name = img.get('alt')
            # 将name中的特殊字符用空格替换掉
            name = re.sub(r'[\.。？\?!！]', '', name)
            suffix = os.path.splitext(img_url)[1]
            img_name = name + suffix
            # 将每个页面获取到的图片名称与URL以元祖的形式放在img_queue队列中
            self.img_queue.put((img_url,img_name))
            print(self.img_queue.get())


class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,img_name = self.img_queue.get()
            print(self.img_queue.get())
            # 判断文件是否存在，如果不存在则进行下载
            if not os.path.isfile(os.path.join(save_path, img_name)):
                request.urlretrieve(img_url, filename=save_path + img_name, reporthook=self.show_percent)
            else:
                print("图片已经存在！")



    def show_percent(self,a, b, c):
        '''回调函数
            @a:已经下载的数据块
            @b:数据块的大小
            @c:远程文件的大小
            '''
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print('%.2f%%' % per)






def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d'% x
        # 将所需爬取页面的url放在队列中
        page_queue.put(url)



    for x in range(5):
        t = Procuder(page_queue,img_queue)
        t.start()


    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()


if __name__ == '__main__':
    main()