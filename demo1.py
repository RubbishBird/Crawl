# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import json
import pandas



    #抓取每页新闻链接
def getNewsLink(url):
    newsdetails = []
    res = requests.get(url)
    print(res.text)
    jd = json.loads(res.text.lstrip('try{feedCardJsonpCallback(').rstrip(');}catch(e){}'))
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails


def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select('.main-title')[0].text
    result['newssource'] = soup.select('.date-source a')[0].text
    result['dt'] = soup.select('.date-source span')[0].text
    # result['dt'] =datetime.strptime(timesource,'%Y年%m月%d日 %H:%M')
    result['article'] = '\n'.join([p.text.strip() for p in soup.select('.article p')[:]])   #等价于以下写法
    # article = []
    # for p in soup.select('.article p')[:]:
    #     article.append(p.text.strip())
    # ' '.join(article)
    result['editor'] = soup.select('.show_author')[0].text.strip('责任编辑：')
    return result



if __name__ == '__main__':
    # newsurl = 'https://news.sina.com.cn/c/2019-06-14/doc-ihvhiqay5553192.shtml'
    url = 'https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4' \
          '&page={}&encode=utf-8&callback=feedCardJsonpCallback&_=1560495860787'
    news_total = []
    i = 1
    # for i in range(1,2):
    newsurl = url.format(i)
    newsaray = getNewsLink(newsurl)
    # news_total.extend(newsaray)
    # df = pandas.DataFrame(news_total)
