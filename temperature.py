#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import requests


def parse_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    reponse = requests.get(url,headers=headers)
    text = reponse.content.decode('utf-8')
    bs = BeautifulSoup(text,'lxml')
    conMidtab = bs.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    city_lowtemp = {}
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            if index == 0:
                city_td = tds[1]
            city_td = tds[0]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
        break



def main():
    url = 'http://www.weather.com.cn/textFC/hb.shtml'
    parse_page(url)




if __name__ == '__main__':
    main()