#!/usr/bin/env python3
#-*- coding:utf-8 -*-

d = [ m + n for m in 'ABC' for n in 'DEF']
print(d)

f = ( m + n for m in 'ABC' for n in 'DEF')
print(f)

# while True:
#     print(next(f))

print('------------------------')
for b in f:
    print(b)


print('斐波那契数列')
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'

fib(6)

print('斐波那契数列')
def fib2(max):
    n,a,b = 0,0,1
    while n < max:
        yield  b
        a, b = b, a+b
        n = n + 1
    return 'done'

f = fib2(6)
print(f)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

print('=================================================')

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

f = odd()
next(f)
next(f)
next(f)
next(f)
next(f)
