# -*- coding: utf-8 -*-
# Time : 2022/4/12 18:17
# Author : Dylan
# File : log.py
# Desc :
import logging

loggers = logging.getLogger()  #创建日志器
loggers.setLevel(logging.INFO)  #定义日志器的级别

f=logging.FileHandler(r'E=D:\pythonxuexi\学习\selenium4\web_unittest_framwork\log',mode='a',encoding='utf-8')#创建处理器
#定义处理器的格式
format=logging.Formatter("%(asctime)s %(filename)s %[line:%(lineno)d] %(linename)s %(message)s")  #定义打印出来的文件格式

f.setLevel(logging.INFO)   #定义级别
f.setFormatter(format)     #定义处理器的格式

loggers.addHandler(f)









