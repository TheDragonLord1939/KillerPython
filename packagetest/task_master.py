#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import random, time, queue

from multiprocessing.managers import BaseManager


task_queue = queue.Queue()
