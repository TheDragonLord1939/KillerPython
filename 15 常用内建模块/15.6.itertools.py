#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import itertools

# natuals = itertools.count(2)
# for n in natuals:
#     print(n)
#     if n == 10:
#         break
#
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

for n in itertools.chain('ABC', )
