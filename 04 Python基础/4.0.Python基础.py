#!/usr/bin/env python3
#print absolute value of an integer

counter = 100
miles = 10000.0
name = 'test'

print(counter)
print(miles)
print(name)

a = b = c = 1
print(a, b, c)

a, b, c = 1, 2, 'test01'
print(a, b, c)


a, b, c, d = 1, 2.3, True, 4+3j
print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))

print("-------------------")
print(a)
del a
# print(a)

print(2/4)

print('=============================')
str = 'Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "TEST")

print(str * 10 * 10)

print('----------------list-----------------')
list = ['abcd', 23, 23.33, 'runoob', 90.9]
tinylist = [123, 'runoob']

print(list)
print(list[0])
print(list[0: 3])
print(list[2:])

print(tinylist * 2)
print(list +tinylist)

print('-------------tuple-----------------')

tuple = ('abc', 333, 2.22, 'runboob', 90.0)
tinytuple = (123, 'runboob')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print((tuple[2:]))
print(tinytuple * 2)
print(tuple +tinytuple)

print('=============================================')
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

if 'Rose' in student:
    print('rose in')
else:
    print('rose not in')

print('==============================================')

a = set('abcdefg')
b = set('defghijkl')
print(a | b)

print('================================================')

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict['two'] = '2 - 菜鸟工具'
tinydict = {'name': 'Tom', 'code': 1, }
print(tinydict)
print(tinydict['name'])
print(tinydict.keys())
print(tinydict.values())

print('====================dict===================================')
bb = dict([('test01', 1), ('test02', 2), ('test03', 3)])
print(bb)
print(dict([('test01', 1), ('test02', 2), ('test03', 3)]))

















