#-*-coding:utf-8-*-

# import re
# #
# # text = "hello ni hao"
# # res = re.split(' ',text)
# # print(res)
#
# text = "today is 20.55 usd"
# r = re.compile(r"""\d+    #匹配数字
#                \.?       #匹配小数点
#                \d*      #匹配数字
#                """,re.VERBOSE)
# res = re.search(r,text)
# print(res.group())



import csv

# with open('abc.csv','r') as fp:
#     reader = csv.reader(fp)
#     titles = next(reader)
#     for x in reader:
#         print(x)

# with open('stock.csv','r') as fp:
#     reader = csv.DictReader(fp)
#     for x in reader:
#         print(x['此处为标题行字段值'])

# headers = ['username','age','height']
# values = [('马超',18,180),
#           ('张飞',28,188),
#           ('赵云',20,185)]
#
# with open('class.csv','w',encoding='utf-8',newline='') as fp:
#     writer = csv.writer(fp)
#     writer.writerow(headers)
#     writer.writerows(values)


# with open('class1.csv','w',encoding='utf-8',newline='') as fp:
#     headers = ['username', 'age', 'height']
#     values = [
#         {'username':'马超','age':18,'height':180},
#         {'username':'赵云','age':19,'height':190},
#         {'username':'李白','age':20,'height':18},
#     ]
#     writer = csv.DictWriter(fp,headers)
#     #写入表头数据的时候，需要调用writeheader方法
#     writer.writeheader()
#     writer.writerows(values)


import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='spider',
    port=3306
)
curser = conn.cursor()
curser.execute("select username from user")
result = curser.fetchone()
print(result)
conn.close()