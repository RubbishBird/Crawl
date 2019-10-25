#-*-coding:utf-8-*-

import pymysql


# 1、连接数据库
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='123456',
#     database='spider',
#     port=3306
# )
# curser = conn.cursor()
# curser.execute("select username from user")
# result = curser.fetchone()
# print(result)
# conn.close()


# 2、插入数据库,方法一
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='123456',
#     database='spider',
#     port=3306
# )
# curser = conn.cursor()
# sql = "insert into user(id,username,age,password) values(1,'kobe',25,123456)"
# curser.execute(sql)
# conn.commit()
# conn.close()

# 2、插入数据库,方法二
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='123456',
#     database='spider',
#     port=3306
# )
# curser = conn.cursor()
# sql = "insert into user(id,username,age,password) values(null,%s,%s,%s)"
# username = 'james'
# age = 23
# password = '666666'
#
# curser.execute(sql,(username,age,password))
# conn.commit()
# conn.close()


# 3、查询数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='spider',
    port=3306
)

curser = conn.cursor()
sql = """
select * from user
"""
curser.execute(sql)
result = curser.fetchall()
print(result)
conn.commit()
conn.close()