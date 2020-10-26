import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
i=0
t5={}
end={}
j=0
k=0
url = "http://w1.97xzjpzz.xyz/pw/thread-htm-fid-15.html"
r0 = requests.get(url,timeout=30)
r1 =BeautifulSoup(r0.content,'lxml')
r2 = r1.find_all('a')
for t2 in r2:
    t3 = t2.get('href')
    try:
        t4=re.findall("html\_data(.+)html",t3)
        if t4!=[]:
            t5[i]=t4
            i=i+1
    except:
        continue
for m in range (int(len(t5)/2)):
    end[j]=t5[k]
    v=str(end[j])
    j=j+1
    k=k+2
    print(v[2:-2])

    

#print(r2[50:100])
            
    
    
