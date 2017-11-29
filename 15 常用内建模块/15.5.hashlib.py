#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('406128445ncl.'.encode('utf-8'))
print(md5.hexdigest())

# 86ef648bbd9d2dcbf74d629cbfdb7792


import  hashlib

sha1 = hashlib.sha1()
sha1.update('406128445ncl'.encode('utf-8'))
print(sha1.hexdigest())
print(len('e219a2a3308ab3d7db5e868f68a48fe469deca7c'))

