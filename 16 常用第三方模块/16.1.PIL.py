#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from PIL import Image

image = Image.open('8d381235jw1e2ofk9u666d31j.jpg')

w,h = image.size
print('Origin image size : %sx%s' % (w,h))



