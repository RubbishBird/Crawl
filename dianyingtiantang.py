#-*-coding:utf-8-*-

from lxml import etree
import requests
import json

BASE_DOMAIN = 'https://www.dytt8.net'
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}


def get_detail_urls(url):
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk','ignore')
    html = etree.HTML(text)
    detail_urls = html.xpath("//ul//table[@class='tbspan']//a/@href")
    detail_urls1 = list(map(lambda url:BASE_DOMAIN + url, detail_urls))
    return detail_urls1

def parse_detail_page(url):
    response = requests.get(url,headers=HEADERS)
    movie = {}
    text = response.content.decode('gbk','ignore')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")
    movie['电影名'] = title
    ZoomE = html.xpath("//div[@id='Zoom']")[0]
    # print(etree.tostring(ZoomE,encoding='utf-8').decode('utf-8'))
    imgs = ZoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['海报'] = cover
    movie['电影截图'] = screenshot
    infos = ZoomE.xpath(".//text()")
    def do_repalce(info,rule):
        return info.replace(rule,'').strip()
    for index,info in enumerate(infos):
        if info.startswith("◎译　　名"):
            info = do_repalce(info,'◎译　　名')
            movie['译名'] = info
        elif info.startswith("◎年　　代"):
            info = do_repalce(info,'◎年　　代')
            movie['年代'] = info
        elif info.startswith("◎产　　地"):
            info = do_repalce(info,'◎产　　地')
            movie['国家'] = info
        elif info.startswith("◎类　　别"):
            info = do_repalce(info,'◎类　　别')
            movie['类别'] = info
        elif info.startswith("◎上映日期"):
            info = do_repalce(info,'◎上映日期')
            movie['上映日期'] = info
        elif info.startswith("◎豆瓣评分"):
            info = do_repalce(info,'◎豆瓣评分')
            movie['豆瓣评分'] = info
        elif info.startswith('◎片　　长'):
            info = do_repalce(info,'◎片　　长')
            movie['电影时长'] = info
        elif info.startswith('◎导　　演'):
            info = do_repalce(info,'◎导　　演')
            movie['导演']= info
        elif info.startswith('◎主　　演'):
            info = do_repalce(info,'◎主　　演')
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith('◎'):
                    break
                actors.append(actor)
            movie['主演'] = actors
        elif info.startswith('◎简　　介 '):
            profiles = []
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                if profile.startswith('【下载地址】'):
                    break
                profiles.append(profile)
            profiles = ''.join(profiles)
            movie['简介'] = profiles
    return movie







def spider():
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for x in range(1,2):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        movies = []
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
        # 存储方式一：
        # 将爬出来的电影转化成json格式
        json_movies = json.dumps(movies,ensure_ascii=False)
        with open('json_movies','w',encoding='utf-8') as fp:
            fp.write(json_movies)

        # 存储方式二：
        # with open('json_movies', 'w', encoding='utf-8') as fp:
        #     json.dump(movies,fp,ensure_ascii=False)


if __name__ == '__main__':
    spider()