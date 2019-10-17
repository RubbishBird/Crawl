#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tencent.html',parser=parser)

bs = BeautifulSoup('tencent.html','lxml')

# 1、获取所有tr标签
# 方法一
# trs = html.xpath('//tr')
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))
# 方法二
# trs = bs.find_all('tr')
# for tr in trs:
#     print(tr)



#2、获取第二个tr标签
# tr = html.xpath('//tr[2]')[1]
# print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))


#3、获取class等于even的tr标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))


#4、获取所有a标签的href属性
# aList = html.xpath("//a/@href")
# for a in aList:
#     print(a)


#5、获取所有的职位信息，纯文本
# trs = html.xpath("//tr[position()>1]")
# positions = []
# for tr in trs:
#     href = tr.xpath(".//a/@href")[0]
#     title = tr.xpath("./td[1]//text()")[0]
#     category = tr.xpath("./td[2]/text()")[0]
#     nums = tr.xpath("./td[3]/text()")[0]
#     address = tr.xpath("./td[4]/text()")[0]
#     pubtime = tr.xpath("./td[5]/text()")[0]
#
#     position = {
#         'url':href,
#         'title':title,
#         'category':category,
#         'nums':nums,
#         'address':address,
#         'pubtime':pubtime
#     }
#     positions.append(position)
# print(positions)
