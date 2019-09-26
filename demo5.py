#-*-coding:utf-8-*-

# 代码实现：将cookie保存到本地

from urllib import request
from http.cookiejar import MozillaCookieJar

def save_cookie():
    cookiejar = MozillaCookieJar('cookie.txt')
    #加载cookie信息s
    cookiejar.load(ignore_discard=True)
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    opener.open('https://www.baidu.com')
    cookiejar.save(ignore_discard=True)          #ignore_discard=True   设置了表示保存即将过期的cookie信息



if __name__ == '__main__':
    save_cookie()