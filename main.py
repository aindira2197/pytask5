import threading
import time
import random

class Hisoblash:
    def __init__(self, son):
        self.son = son

    def hisobla(self):
        print(f"Hisoblash boshlandi: {self.son}")
        time.sleep(random.randint(1, 5))
        natija = self.son * self.son
        print(f"Hisoblash tugadi: {self.son} ^ 2 = {natija}")

def parallel_hisoblash(sonlar):
    threads = []
    for son in sonlar:
        hisob = Hisoblash(son)
        thread = threading.Thread(target=hisob.hisobla)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def asosiy():
    sonlar = [i for i in range(1, 11)]
    parallel_hisoblash(sonlar)

asosiy()

import concurrent.futures

class ParallelHisoblash:
    def __init__(self, son):
        self.son = son

    def hisobla(self):
        print(f"Hisoblash boshlandi: {self.son}")
        time.sleep(random.randint(1, 5))
        natija = self.son * self.son
        print(f"Hisoblash tugadi: {self.son} ^ 2 = {natija}")
        return natija

def parallel_hisoblash_concurrent(sonlar):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(ParallelHisoblash(son).hisobla) for son in sonlar]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

def asosiy_concurrent():
    sonlar = [i for i in range(1, 11)]
    parallel_hisoblash_concurrent(sonlar)

asosiy_concurrent()