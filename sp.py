import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
t={}
a=0
#http://p7.urlpic.club/pic1893/upload/image/20190130/13010126159.jpg
def getnumber(a):
    b=0
    for i in range(a):
        
        if i<=9:
            b='00'+str(i)
            yield b
            i=i+1
        if i<=99 and i>=10:
            b='0'+str(i)
            yield b
            i=i+1
        if i>100:
            b=i
            yield b
            i=i+1
        
    #yield i
        
#getnumber(150)
for q in getnumber(1000):
    url='http://p7.urlpic.club/pic1893/upload/image/20190130/13010126'+str(q)+'.jpg'
    path="D:/s8/%s.jpg"%a
    try:
        r2=requests.get(url)
    except:
        continue
    print(a)
    a=a+1
    with open(path,'wb') as f:
        f.write(r2.content)
        f.close()
    

