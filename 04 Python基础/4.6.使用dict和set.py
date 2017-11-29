#!/usr/bin/env python3
#-*- coding:utf-8 -*-

persons = {'test01':99,'test02':88,'test03':33}

print(persons)

print(persons['test01'])

persons['test04'] = '77'
print(persons)

print(persons['test01'])

print('test01' in persons)
print('test05' in persons)
print(persons.get('test05'))
print(persons.get('test05',66))

print(persons)
print(persons.pop('test01'))
print(persons)

print('======================================================')

s = set([1,2,3])
print('s = ' , s)

s.add(4)
print('s = ' , s)
s.add(4)
print('s = ' , s)

s.remove(3)
print(s)



