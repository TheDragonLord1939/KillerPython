#!/usr/bin/env python3
#-*- coding:utf-8 -*-

names = ['test01','test02','test03']
for name in names:
    print(name)

classes = ['class01','class02','class03']
for i in list(range(3)):
    print(names[i])

a = range(3)
print(list(a))

sum = 0
for num in list(range(101)):
    sum = sum + num
print("sum = %d" % sum)

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print("sum = ", sum)


print('------------------------------------------------------')
# n = 0
# while True:
#     if n > 10:
#         continue
#     n = n + 1
#     print (n)

print('--------------------------------------------------------')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)











