#-*-coding:utf-8-*-
from lxml import etree
import requests

'''
    response.text：返回的是一个经过解码后的字符串，是str(unicode)类型
    response.content：返回的是一个原生字符串，就是从网页上抓取下来的，没有经过处理的字符串，是bytes类型
'''

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}


def parse(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text  # 或者这种写法也可以：text = response.content.decode('utf-8','ignore')
    html = etree.HTML(text)
    divs = html.xpath("//div[@class='main review-item']")
    comment = []
    for div in divs:
        author = div.xpath(".//a[@class='name']/text()")[0]
        star_level = div.xpath(".//span[contains(@class,'main-title-rating')]/@title")[0]
        comment_detail = {
            '昵称':author,
            '推挤指数':star_level
        }
        comment.append(comment_detail)


def get_detail_comment():
    url = 'https://movie.douban.com/j/review/10598819/full'
    response = requests.get(url,headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    text = html.xpath("//pre/text()")
    # print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
    print(text)


if __name__ == '__main__':
    base_url = 'https://movie.douban.com/subject/30166972/reviews?start={}'
    id = [0]
    for x in id:
        url = base_url.format(x)
    # parse(url)
    get_detail_comment()