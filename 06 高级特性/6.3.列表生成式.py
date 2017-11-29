#!/usr/bin/env python3
#-*- coding:utf-8 -*-

for i in range(11):
    print(i)

print('------')
for i in list(range(11)):
    print(i)

print('------')
k = []
for i in list(range(11)):
    k.append(i * i)
print(k)

print('------------------')
b = [x * x for x in range(0,11)]
print(b)

m = [x * x for x in range(0,11) if x % 2 == 0]
print(m)

print('------------------------')
q = [m + n for m in 'ABC' for n in 'DEF']
print(q)

print('-------------------------------')
import os
print([d for d in os.listdir('.')])

print('---------------------------------')
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)

b = [k+'='+v for k,v in d.items()]
print(b)

d = {'Hello', 'World', 'IBM','Apple'}
f = [j.lower() for j in d]
print(f)
print('==================================')
d = ['Hello', 'World', 99, 'IBM','Apple']
print([p.lower() for p in d if isinstance(p, str) ])
print([w.lower for w in d])

