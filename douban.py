#-*-coding:utf-8-*-

import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Referer':'https://movie.douban.com/'
}

url = 'https://movie.douban.com/cinema/nowplaying/nanjing/'

response = requests.get(url,headers=headers)
text = response.text

html = etree.HTML(text,parser=etree.HTMLParser(encoding='utf-8'))
movies = []
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
for li in lis:
    title = li.xpath("@data-title")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    href = li.xpath(".//img/@src")[0]

    movie = {
        "title":title,
        'duration':duration,
        'region':region,
        "director":director,
        "actors":actors
    }
    movies.append(movie)
print(movies)