import time
a = (time.strftime("%Y年%m月%d日%H时%M分%S秒", time.localtime(time.time())))
print(a)
