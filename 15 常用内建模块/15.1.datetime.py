#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from datetime import datetime

now = datetime.now()
print('now', now)

now = datetime(2017, 11, 12, 15, 36, 22)
print('now', now)
print('now', now.timestamp())

now = datetime.now()
print('now',now.timestamp())

time = 1510212059.105638
print(datetime.fromtimestamp(time))

cday = datetime.strptime('2017-10-11 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

datetime_now = datetime.now()
strftime = now.strftime('%a, %b %d %H:%M')
print(strftime)

print('-----------------------------------------------')
from datetime import timedelta

d = datetime.now()
print(d)
d = d + timedelta(days = 1)
print(d)