# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s) '% (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()




# import time, threading
#
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_thread, args=(55,))
# t2 = threading.Thread(target=run_thread, args=(88,))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print(balance)



# import time, threading
#
# def loop():
#     print('thread %s is running....' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)












# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print()













# import threading
# import time
#
# exitFlay = 0
#
# class myThread(threading.Thread):
#
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print("退出线程：" + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlay:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s:%s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(1, "Thread-2", 2)
#
# thread1.start()
# thread2.start()
# thread2.join()
# thread1.join()
#
#
# print("退出主线程")














# import _thread
# import time
#
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s : %s" % (threadName, time.ctime(time.time())))
#
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2, ))
#     _thread.start_new_thread(print_time, ("Thread-2", 4, ))
# except:
#     print("Error: 无法启动线程")
#
# while 1:
#     pass








