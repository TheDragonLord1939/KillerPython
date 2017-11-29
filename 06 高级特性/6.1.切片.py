#!/usr/bin/env python3
#-*- coding:utf-8 -*-

L = ['test01', 'test02', 'test03']
print(L[0],L[1],L[2])

r = []
for n in range(3):
    r.append(L[n])

print(r)

print(L[0:2])
print(L[:3])
print(L[1:2])
print(L[-2])

k = []
for n in range(100):
    k.append(n)

print(k[0:101:2])
print(k[::5])
print(k[:])

t = (0,1,2,3,4,5)
print(t[:3][2])

str = 'hello world !'
print(str[:5])