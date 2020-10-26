from multiprocessing.dummy import Pool as ThreadPool
import requests
file=open("D:/pictureurl.txt")
lis = []
i=0
k=0
for line in file.readlines():
    lis.append(line)
def spider(url):
    a=url[0:-1]
    pic=requests.get(a)
    
    path="d://s11//%s.jpg" %url[-10:-5]
    print(a)
    with open(path,'wb') as f:
        f.write(pic.content)
        f.close()

pool=ThreadPool(2)
pool.map(spider,lis)
pool.close()
pool.join()

