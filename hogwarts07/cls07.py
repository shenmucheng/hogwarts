import os

# os.mkdir("testone")

print(os.listdir())
# os.removedirs("testone")
# 下面获取地址可以用来创建文件、删除文件等一系列操作
print(os.getcwd())
# 下面打印结果==false，就说明b文件不存在
print(os.path.exists("b"))
if not os.path.exists("b"):
    os.makedirs("b")
if not os.path.exists("b/test.txt"):
    f = open("b/test.txt","w")
    f.write("hello,os using")
    f.close()


# ################time标准库练习####################
import time

print("方法一：国外的时间格式>",time.asctime())
# 从纪元开始到现在的一个秒数：从时代为1970年1月1日00:00:00，开始计算
print("方法二：时间戳>",time.time())
# print(time.sleep())
print("方法三：时间戳转成时间元组>",time.localtime())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前的时间
now_timestamp = time.time()
two_day_before = now_timestamp - 60*60*24*2
time_tuple = time.localtime(two_day_before)
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))


# python2中的时候
import urllib2
response=urllib2.urlopen("http://www.baidu.com")

# python3的时候,将urllib封装到request里面
import urllib.request
response=urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.read())


# math用于科学计算的库
import math

print(math.ceil(5.5))
print(math.ceil(4.4))
print(math.floor(5.5))
print(math.sqrt(36))