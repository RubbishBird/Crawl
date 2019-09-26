#-*-coding:utf-8-*-

#代码功能：获取cookie

import requests

#verify=False,用于处理不被信任的SSL网站
# response = requests.get('http://www.baidu.com/',verify=False)
# print(response.cookies)



#session相关用法
url= 'http://jira.vemic.com/login.jsp'
data = {
    'os_username':'weifeng',
    'os_password':'weifeng520!'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

session = requests.session()
session.post(url,data=data,headers=headers)
response = session.get('http://jira.vemic.com')
with open('jira.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))
