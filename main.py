import threading
import time
import random

class HisoblashDasturi:
    def __init__(self):
        self.natija = 0

    def hisoblash(self, son):
        for i in range(son):
            self.natija += i
            time.sleep(0.001)

    def parallel_hisoblash(self, sonlar):
        threads = []
        for son in sonlar:
            thread = threading.Thread(target=self.hisoblash, args=(son,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

def asosiy():
    dastur = HisoblashDasturi()
    sonlar = [100, 200, 300, 400, 500]
    dastur.parallel_hisoblash(sonlar)
    print(dastur.natija)

def boshqa_funksiya():
    for i in range(10):
        print(i)
        time.sleep(0.5)

class BoshqaDastur:
    def __init__(self):
        self.natija = 0

    def hisoblash(self, son):
        for i in range(son):
            self.natija += i
            time.sleep(0.001)

    def parallel_hisoblash(self, sonlar):
        threads = []
        for son in sonlar:
            thread = threading.Thread(target=self.hisoblash, args=(son,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

def boshqa_asosiy():
    dastur = BoshqaDastur()
    sonlar = [100, 200, 300, 400, 500]
    dastur.parallel_hisoblash(sonlar)
    print(dastur.natija)

class UchinchiDastur:
    def __init__(self):
        self.natija = 0

    def hisoblash(self, son):
        for i in range(son):
            self.natija += i
            time.sleep(0.001)

    def parallel_hisoblash(self, sonlar):
        threads = []
        for son in sonlar:
            thread = threading.Thread(target=self.hisoblash, args=(son,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

def uchinchi_asosiy():
    dastur = UchinchiDastur()
    sonlar = [100, 200, 300, 400, 500]
    dastur.parallel_hisoblash(sonlar)
    print(dastur.natija)

thread1 = threading.Thread(target=asosiy)
thread2 = threading.Thread(target=boshqa_asosiy)
thread3 = threading.Thread(target=uchinchi_asosiy)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()