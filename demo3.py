#-*-coding:utf-8-*-

from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

# 动态获取登录cookie demo

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

def get_opener():
    # 管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失
    cookiejar = CookieJar()

    # HTTPCookieProcessor使用CookieJar对象，将不同类型的CookieJar对象作为HTTPCookieProcessor的参数提供，可支持不同的cookie处理
    handler = request.HTTPCookieProcessor(cookiejar)

    # 基本的urlopen()函数不支持验证、cookie或其他HTTP高级功能。要支持这些功能，必须使用build_opener()函数来创建自己的自定义Opener对象
    opener = request.build_opener(handler)
    return opener

def login(opener):
    data = {
        'os_username':'weifeng',
        'os_password':''
    }
    login_url = 'http://jira.vemic.com/login.jsp'
    res = request.Request(login_url,headers=headers,data=parse.urlencode(data).encode('utf-8'))
    opener.open(res)

def visit(opener):
    url = 'http://jira.vemic.com'
    req = request.Request(url,headers=headers)
    resp = opener.open(req)
    with open('jira.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login(opener)
    visit(opener)

# cookieStr = ''
# for item in cookiejar:
#     cookieStr = cookieStr + item.name + '=' + item.value + ';'
# print(cookieStr)


