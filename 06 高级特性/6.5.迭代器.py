#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from collections import Iterable

print(isinstance([], Iterable))

print(isinstance({}, Iterable))

print(isinstance('abc', Iterable))

print(isinstance((x for x in range(10)),Iterable))

print(isinstance(100, Iterable))

it = iter([1,2,3,4,5])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break