#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def my_abs(s):
    if s >= 0:
        return s
    else:
        return -s

print(my_abs(-9999))

def nop():
    pass
print(nop())


def my_abs_new(x):
    if not isinstance(x,(int,float)):
        return TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

print(my_abs_new(-99999))
print(my_abs_new('39393993'))

def double_return(x):
    return x,x
a,b = double_return(888)
print(a,b)
print(double_return(999))


