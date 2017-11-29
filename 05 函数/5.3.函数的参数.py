#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def power(x):
    return x*x
print(power(15))


def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(15,3))

print(power(5))

def add_end(L = []):
    L.append('end')
    return L
print(add_end([1,2,3]))
print(add_end([1,2,3,4]))

print(add_end())
print(add_end())

def add_end(L = None):
    if L is None:
        L = []
    L.append('end')
    return L
print("------")

print(add_end([1,2,3]))
print(add_end())
print(add_end())

print("=======================================================================")

def calc(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num * num
    return sum

print(calc([1,2,3]))
print(calc([1,2,3,4]))

def calc_new(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num * num
    return sum

print(calc_new(1,2,3))

def calc_new_new(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num * num
    return sum
print('==>' , calc_new_new(*[1,2,3,4,5]))

print('----------------------关键字参数-----------------------------')
def student_inf(name, age, **other):
    print('name',name,'age',age,'other',other)

student_inf('test01', 19)
student_inf('test01',29,city='bj',tele='123445')

stus = {'city':'bj','tele':12344}
student_inf('test02',29,**stus)

print('-----------------------命名关键字参数------------------------------------')
def student_inf(name, age, *, city, tele):
    print('name',name,'age',age,'city',city,'tele',tele)
student_inf('test01',22,city='bijing',tele=12333)

def student_inf(name, age, *number,city,addr):
    print('name',name)
    print('age',age)
    for n in number:
        print(n)

    print('city',city)
    print('addr',addr)

student_inf('test09',22,*[1,2,3,4],city='bj',addr = 12306)
