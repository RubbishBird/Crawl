#-*-coding:utf-8-*-

from lxml import etree
import requests


HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}

def get_detail_urls(url):
    response = requests.get(url,headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    print(etree.tostring(html,encoding='utf-8').decode('utf-8'))


if __name__ == '__main__':
    url = 'https://careers.tencent.com/search.html?index=1&keyword=python'
    get_detail_urls(url)