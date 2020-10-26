import random
import threading
from time import ctime,sleep

'''for i in range (1000):
    a = random.randint(0,9)

    b= random.randint(0,99)

    c=random.randint(1,2)
   
    if int(c) == 1:
        t='+'
    else:
       t='-'
    print(b,t,a,"=")
'''
'''def num1():
    for i in range(1000):
        a=random.randint(0,9)
    return a

class MyThread(threading.Thread):
    def __init__(self,func,args):
        super(MyThread,self).__init__()
        self.func=func
        self.args=args
    def run(self):
        self.result=self.func(*self.args)
    def get_result():
        try:
            return self.result
        except Exception:
            return None


def getnum():
    a=random.randint(0,9)
    b=random.randint(0,99)
    c=random.randint(1,2)
    return a,b,c
li = []
for i in range(10):
    t=MyThread(getnum,None)
    li.append(t)
    t.start()

for t in li:
    t.join()
    print (t.get_result())
'''






    
