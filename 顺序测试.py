from multiprocessing.dummy import Pool as ThreadPool
import requests
file=open("D:/pictureurl.txt")
file2=open("D:/pictureurl1.txt")
lis = []
lis1= []
k=0
for line in file.readlines():
    a=line[:-1]
    lis.append(a)
    

for line2 in file2.readlines():
    b= line[:-1]
    lis1.append(b)
def spider(url):
    try:
        pic=requests.get(url,timeout=10)
        if(pic.status_code==200):
            print('并发1')
            print(pic.status_code,pic.url)
    except:
        pass
    

def spider1(url1):
    try:
        pic1=requests.get(url1,timeout=10)
        if(pic1.status_code==200):
            print('并发2')    
            print(pic1.status_code,pic1.url)
    except:
        pass
pool =ThreadPool(4)
pool.map(spider,lis)
pool.map(spider1,lis1)
pool.close()
pool.join()
