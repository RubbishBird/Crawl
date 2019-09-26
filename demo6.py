#-*-coding:utf-8-*-


#代码功能：初步接触requests库

import requests

#get请求
def get_method():
    params = {
        'wd':'中国'
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    response = requests.get('https://www.baidu.com',params=params,headers=headers)
    with open('baidu.html','w',encoding='utf-8') as fp:
        fp.write(response.content.decode('utf-8'))

    print(response.url)

#post请求
def post_method():

    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
        'first':'true',
        'pn':'1',
        'kd':'python'
    }

    proxy = {
        'http':'171.14.209.180:2782'
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    }

    response = requests.post(url,data=data,headers=headers,proxies=proxy)
    print(response.content.decode('utf-8'))












if __name__ == '__main__':
    # get_method()
    post_method()
