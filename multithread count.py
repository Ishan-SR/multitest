
from threading import *
import time

score = 0

class thrfirst(Thread):
    def run(self):
        while (time.time()-initial_time<1):
            score = score +1

class thrsec(Thread):
    def run(self):
        while (time.time()-initial_time<1):
            score = score +1

class thrthi(Thread):
    def run(self):
        while (time.time()-initial_time<1):
            score = score +1

class thrfou(Thread):
    def run(self):
        while (time.time()-initial_time<1):
            score = score +1


t1=thrfirst()
t2=thrsec()
t3=thrthi()
t4=thrfou()


initial_time=time.time()

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print(score)

time.sleep(4)
