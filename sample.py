
import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime
import pandas

# url = 'http://news.sina.com.cn/china/'
# r= requests.get(url)
# r.encoding = 'utf-8'
# soup = BeautifulSoup(r.text,'html.parser')
# # print(soup)
#
# for news in soup.select('.news-2'):
#     len = len(news.select('li'))
#     i = 0
#     while i<len:
#         title = news.select('li')[i].text
#         a = news.select('a')[i]['href']
#         print(title,a)
#         i = i+1

#获取文章内容
# url = 'https://news.sina.com.cn/c/2019-06-14/doc-ihvhiqay5553192.shtml'
# r = requests.get(url)
# r.encoding = 'utf-8'
# soup = BeautifulSoup(r.text,'html.parser')
#
# # article = []
# # for p in soup.select('.article p')[:-1]:
# #     article.append(p.text.strip())
# # '\n'.join(article)
# # 以上写法等价于如下写法：
# aritcle = '\n'.join([p.text.strip() for p in soup.select('.article p')[:-1]])
# print(aritcle)

# 取得编辑人员字段名
# url = 'https://news.sina.com.cn/c/2019-06-14/doc-ihvhiqay5553192.shtml'
# r = requests.get(url)
# r.encoding = 'utf-8'
# soup = BeautifulSoup(r.text,'html.parser')
#
# author = soup.select('.show_author')[0].text.strip('责任编辑：')
# print(author)

#获取新闻ID,对新闻链接进行切割
# newsurl = 'https://news.sina.com.cn/c/2019-06-14/doc-ihvhiqay5553192.shtml'
# a = newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
# print(a)
#
# # 等价于
# m = re.search('doc-i(.*).shtml',newsurl)
# print(m.group(1))

commentURL = 'https://cre.mix.sina.com.cn/api/v3/get?callback=jQuery111108346960723909649_1560490933444&' \
             'cateid=sina_all&cre=tianyi&mod=pcpager_china&merge=3&statics=1&this_page=1&length=40&up=0&down=0&page' \
             'url=https%3A%2F%2Fnews.sina.com.cn%2Fc%2F2019-06-13%2Fdoc-ihvhiqay5492580.shtml&imp_type=2&action=0&' \
             'fields=media%2Cauthor%2Clabels_show%2Ccommentid%2Ccomment_count%2Ctitle%2Cltitle%2Curl%2Cinfo%2Cthumbs' \
             '%2Cthumb%2Cctime%2Creason%2Ccategory%2Cvideo_id%2ChotTag%2Cimg_count%2Cgif%2Clive_stime%2Clive_etime%2' \
             'Cmedia_id%2Csummary%2CorgUrl%2Cshow%2Cintro%2Cdocid%2Cplaytimes%2Cvideo_height%2Cvideo_width%2Ctime_length%2Cuser_icon%' \
             '2Cuid&tm=1560490940&offset=0&ad=%7B%22rotate_count%22%3A100%2C%22platform%22%3A%22pc%22%2C%22channel%22%3A%22' \
             'tianyi_pcpager_china%22%2C%22page_url%22%3A%22https%3A%2F%2Fnews.sina.com.cn' \
             '%2Fc%2F2019-06-13%2Fdoc-i{}.shtml%22%2C%22timestamp%22%3A1560490940536%7D&_=1560490933450'

url= 'https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4' \
     '&page={}&encode=utf-8&callback=feedCardJsonpCallback&_=1560495860787'

def getCommentConuts(newsurl):
    m = re.search('doc-i(.*).shtml',newsurl)
    newsId = m.group(1)
    comments = requests.get(commentURL.format(newsId))
    jd =json.loads(comments.text.strip('data='))
    # print(jd)
    return jd['total']

newsurl = 'https://news.sina.com.cn/c/2019-06-14/doc-ihvhiqay5553192.shtml'
getCommentConuts(newsurl)

#抓取内文信息
def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text
    result['newssource'] = soup.select('.time-source span a')[0].text
    timesource = soup.select('.time-source')[0].contents[0].strip()
    result['dt'] = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.strip('责任编辑：')
    result['comments'] = getCommentConuts(newsurl)
    return result


#抓取每页的新闻链接
def parseListLinks(url):
    newsdetails = []
    res = requests.get(url)
    jd = json.loads(res.text.lstrip('newsloadercallback(').rstrip(');'))
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails

if __name__ == '__main__':
    news_total = []
    for i in range(1,3):
        newsurl = url.format(i)
        newsary = parseListLinks(newsurl)
        news_total.extend(newsary)