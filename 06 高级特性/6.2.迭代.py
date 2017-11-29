#!/usr/bin/env python3
#-*- coding:utf-8 -*-

d = {'name':'test01','age':99}
for i in d:
    print(i)

print('======')
for m in d.values():
    print(m)

print('======')
for m in d.items():
    print(m)


print('===================')
for m in 'hello world':
    print(m)


print('===================')
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

print('===================')
for i,value in enumerate(['a','b','c']):
    print(i,value)

print('======================')
for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)