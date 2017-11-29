#!/usr/bin/env python3
#-*- coding:utf-8 -*-
classmates = ['Dragon01','Dragon02', 'Dragon03']
print(classmates)

print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])
# print(classmates[3])


print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

classmates.append('Dragon04')
print(classmates)
print(classmates.pop(2))
print(classmates)

print('---------------------------')
print(classmates)
classmates[2]='dragon03'
print(classmates)


L = ['apple',123,True]
print(L)

s = ['python','java',['k1','k2']]
print(s[2][0])

print('------tuple----------')
t = (1,2)
print(t)

t = ()
print(t)

t = (1)
print(t)

t = (1,)
print(t)

t = ('dragon01','dragon02',['fuck1','fuck02'])
print(t)
t[2][0] = 'good01'
t[2][1] = 'good02'
print(t)













