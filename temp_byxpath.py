#-*-coding:utf-8-*-

import requests
from lxml import etree

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

def parse_page(url):
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    html = etree.HTML(text)
    conMidtab = html.xpath("//div[@class='conMidtab']")[0]
    # print(etree.tostring(conMidtab,encoding='utf-8').decode('utf-8'))
    tables = conMidtab.xpath(".//table")
    city_mintemp = {}
    for table in tables:
        trs = table.xpath("tr")[2:]
        for index,tr in enumerate(trs):
            if index == 0:
                city = tr.xpath(".//td//a/text()")[1]
            else:
                city = tr.xpath(".//td//a/text()")[0]
            min_temp = tr.xpath(".//td/text()")[-2]
            city_mintemp[city] = min_temp
    return city_mintemp



def main():
    # urls = ['http://www.weather.com.cn/textFC/hb.shtml','http://www.weather.com.cn/textFC/db.shtml','http://www.weather.com.cn/textFC/hd.shtml','http://www.weather.com.cn/textFC/hz.shtml'
    #         ,'http://www.weather.com.cn/textFC/hn.shtml','http://www.weather.com.cn/textFC/xb.shtml','http://www.weather.com.cn/textFC/xn.shtml']
    urls = ['http://www.weather.com.cn/textFC/gat.shtml']
    for url in urls:
        city = parse_page(url)
        print(city)
        print('='*30)


if __name__ == '__main__':
    main()