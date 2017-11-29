# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql.cursors

#连接数据库
connect = pymysql.Connect(
    host='node3',
    port=3306,
    user='root',
    passwd='123456',
    db='test',
    charset='utf8'
)

#获取游标
cursor = connect.cursor()

# #插入数据
# sql = "insert into trade (name, account, saving) values ('%s','%s',%.2f)"
# data = ('雷军', '12542122364422300', 1000)
# cursor.execute(sql % data)
# connect.commit()
# print('成功插入', cursor.rowcount, '条数据')
#
# #修改数据
# sql = "update trade set saving = %.2f where account = '%s'"
# data = (8888,'12533654895')
# cursor.execute(sql % data)
# connect.commit()
# print('成功修改', cursor.rowcount, '条数据')
#
# #查询数据
# sql = "select id, name,saving from trade where account = '%s'"
# data = ('12542122364',)
# cursor.execute(sql % data)
# for row in cursor.fetchall():
#     print("id:%d\tName:%s\tSaving:%.2f" % row)
# print('共查找出', cursor.rowcount, '条数据')
#
# #删除数据
# sql = "delete from trade where id = %d "
# data = (1,)
# cursor.execute(sql % data)
# connect.commit()
# print('成功删除', cursor.rowcount, '条数据')

#事物处理
sql_1 = "update trade set saving = saving + 7777 where id = 7"
sql_2 = "update trade set expend = expend + 7777 where id = 7"
sql_3 = "update trade set income = income + 999999999999999999999999 where id = 7"

try:
    cursor.execute(sql_1)
    cursor.execute(sql_2)
    cursor.execute(sql_3)
except Exception as e:
    connect.rollback()
    print('error',e)
else:
    connect.commit()
    print('success', cursor.rowcount)

#关闭连接
cursor.close()
connect.close()







