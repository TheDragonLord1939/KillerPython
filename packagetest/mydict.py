#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def stu2Dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

def dict2Stu(d):
    return Student(d['name'], d['age'], d['score'])

if __name__ == '__main__':
    s = Student('Bob', 20, 88)
    print(json.dumps(s, default=lambda obj: obj.__dict__))

    str = '{"name": "Bob", "age": 20, "score": 88}'
    print(json.loads(str, object_hook=dict2Stu).name)






# import json
#
# d = dict(name='Test01', age=29, score=99)
# print(json.dumps(d))
# print('type %s' % type(json.dumps(d)))
#
# json_str = '{"name": "Test01", "age": 29, "score": 99}'
# print(json.loads(json_str))
# print('type', type(json.loads(json_str)))




#
# import os
#
# print([x for x in os.listdir('.') if os.path.isfile(x) and  os.path.splitext(x)[1] == '.txt'])























# import os
#
# print(os.listdir('.'))
#
#
#
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x)])
#
#
# print()














# import os
#
# print(os.path.abspath('.'))
#
#
# # os.mkdir('./testdir')
#
# os.path.join('./testdir', 'indir')











# )import os
#
# print(os.name)
# # print(os.uname())
#
# print(os.environ)
# print(os.environ.get('PATH')











# from io import StringIO
#
# s = StringIO()
# s.write('hello')
# s.write(' ')
# s.write('world')
#
# print(s.getvalue())










# with openpri(r'C:\Users\TheDragonLord\Desktop\999999_copy', 'w') as write:
#
#     with open(r'C:\Users\TheDragonLord\Desktop\999999', 'r') as f:
#         while True:
#             line = f.readline()
#             write.write(line)
#             if line == '':
#                 break


# with open('./word.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())






#
# with open('./word.txt', 'r') as f:
#     print(f.read(9))
#
# if f:
#     print ('fuck')


# try:
#     f = open('./word.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()




# f = open('./word.txt', 'r')
# print(f.read())
# f.close()




















