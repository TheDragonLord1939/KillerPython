# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('create table user(id varchar(20) primary key ,name varchar (20))')

cursor.execute('insert into user(id, name) values (\'1\',\'Michael\')')
cursor.rowcount
cursor.close()
conn.commit()
conn.close()

print('创建成功')

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id = ?',('1',))

values = cursor.fetchall()
print('value=',values)

cursor.close()
conn.close()








