#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


if __name__ == '__main__':
    b1 = Student('test01', 59)
    b2 = Student('test02', 33)

    b1._Student__name = 'test03'

    print(b1.get_name())
    print(b1._Student__name)

















#
# 'a test module'
#
# __author__ = 'Dragon'
#
# import sys
#
# def test():
#     print('args=', sys.argv)
#
# if __name__ == '__main__':
#     test()


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now(x):
#     print(x)
#
# now(2018)

# def now():
#     print('2017')
#
# f = now
# f()
#
# print(f.__name__)





# def bulid(x, y):
#     return lambda: x * x + y * y
#
# print(bulid(1, 2))
# print(bulid(1, 2)())









# from functools import reduce
#
#
# l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(l)
#
# a = reduce(lambda m, n: m + n, l)
# print(a)
#
#
# d






#
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print(type(f))
#
# print(f())
















# print(sorted([36, 5, -12, 9, 21]))
#
# print(sorted([36, 5, 12, -20], key=abs))
#
# b = sorted([1, 4, 2, 5, 9, 7], reverse=True)
# print(b)














# def is_odd(n):
#     return n % 2 == 1
#
# print(list(filter(is_odd, list(range(11)))))
#
#
# def not_empty(s):
#     return s and s.strip()
#
# print(list(filter(not_empty, ['A', '', 'B'])))
















# from functools import reduce
#
# def add(x, y):
#     return x + y
#
# print(reduce(add, list(range(101))))
#
#
# print(list(map(str, list(range(101)))))

















# def f(x):
#     return x * x
#
# r = map(f, list(range(11)))
# print(list(r))
#
# print(list(range(10)))
#
# print(list(map(str, list(range(11)))))


# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-5, 6, abs))


# list = [1, 2, 3, 4]
# it = iter(list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# import  sys
# list = [1, 2, 4, 5]
# it = iter(list)
#
# while True:
#     print(next(it))













# def odd():
#     print('step 1')
#     yield
#     print('step 2')
#     yield
#     print('step 3')
#     yield
#
# o = odd()
# next(o)
# next(o)
# next(o)
# next(o)












# L = [x * x for x in range(10)]
# print(L)
#
# L = (x * x for x in range(10))
# print(L)
#
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# d = {'x': 'A', 'y':'B', 'z':'C'}
# for k, v in d.items():
#     print(k, '=', v)

# print([x * x for x in list(range(1, 11))])
#
#
# import os
# print([d for d in os.listdir('.')])

# d = {'a':1, 'b':2, 'c':3}
# for dd in d:
#     print(d[dd])

# d = [1, 23, 3, 4, 5]
# for dd in d:
#     print(dd)

# d = (1,2,34,4)
# for dd in d:
#     print(dd)

# for d in list(range(11)):
#     print(d)

# for d in range(11):
#     print(d)



# for i, value in enumerate(['a', 'b', 'c']):
#     print(i, value)




# L = ['test01', 'test02', 'test03']
#
# print(L)
#
# print(L[0:2])
#
# L = list(range(100))
# print(L)
#
# tuple1 = (0, 1, 2, 3, 4)
# print(tuple1[:3])

# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n = n + 2
#
# print(L)


# def person():
#     pass
#
# print(type(person()))

# def person(name, age, **kw):
#     print('name:', name, 'age', age, 'other', kw)
#
# print(person('test01', 22, addr='bj', tele=1234545))

#
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc([1, 2, 3, 4]))
#
# list1 = [1, 2, 3, 4, 5, 6]
# print(calc(list1))


# def calc_new(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc_new(1, 2, 3, 4))
#
# list1 = [1, 2, 3, 4]
# print(calc_new(*list1))




# def power(x):
#     print("------------------------")
#     return x * x


# def power(x, n=2):
#     print("=============================")
#     s = 1
#     while n > 0:
#         n = n -1
#         s = s * x
#     return s
#
# print(power(25))












# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# print(calc(1, 2))

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc(list(range(1,10))))


# def power(x):
#     return x * x
#
# print(power(5))
# print(power(15))



# for i in range(5):
#     print(i)


# for i in range(5):
#     print(i)


# flag = 1
# while (flag): print('欢迎访问菜鸟教程')
# print("Good bye!")

# count = 0
# while count < 5:
#     print(count, 'smaller than 5')
#     count = count + 1
# else:
#     print(count, 'bigger than 5')

# n = 100
#
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
#
# print("1 to %d 之和为： %d" % (n, sum))

# list1 = ['test01', 'test02', 'test03']
# tuple1 = ('test01', 'test02', 'test03')
# dict1 = {'name': 'test01', 'age': 88}
# for n in list1:
#     print(n)
#
# for m in tuple1:
#     print(m)
#
# for d in dict1:
#     print(dict1[d])

# var1 = 100
# if var1:
#     print("one")
#     print(var1)
#
# var2 = 0
# if var2:
#     print("two")
#     print(var2)
#

# age = int(input("请输入你家狗狗的年龄： "))
# print(" ")
# if age < 0:
#     print("你他妈在逗我吧！")
# elif age == 1:
#     print("24age")
# elif age == 2:
#     print("22age")
# elif age > 2:
#     print("2age")
#
# input("点击Enter键退出")
