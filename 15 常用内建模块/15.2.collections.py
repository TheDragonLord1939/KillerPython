#!/usr/bin/env python3
#-*- coding:utf-8 -*-

p = (1,2)
print(p)

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)

print(p.x)
print(p.y)

print(isinstance(p,Point))
print(isinstance(p,tuple))

c = namedtuple('Circle', ['x', 'y', 'r'])
k = c(1,2,3)
print(k.x)
print(k.y)
print(k.r)


from collections import deque
q = deque(['a','b','c'])
q.append('d')
q.appendleft(0)
print('q', q)

from collections import defaultdict
dd = defaultdict(lambda:'N/A')

dd['kk'] = 'bb'
print(dd['kk'])

print(dd['ff'])

print('-----------OrderedDict----------------')
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys())

print('-----------------------------------------')
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print('c',c)