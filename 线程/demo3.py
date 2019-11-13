#-*-coding:utf-8-*-

import time
import threading
import random


'''
Lock()用法
'''

gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTotalTimes
        global gTimes
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gTimes >= gTotalTimes:
                gLock.release()
                break
            gMoney += money
            print("%s线程生产了%d元钱，剩余%d元钱"%(threading.current_thread(),money,gMoney))
            gTimes += 1
            print(gTimes)
            gLock.release()
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gTotalTimes
        global gTimes
        while True:
            money = random.randint(300,1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print("%s线程消费了%d元钱，剩余%d元钱" % (threading.current_thread(), money, gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
                print("%s消费者消费了%d元钱，还剩%d元钱，不足！"%(threading.current_thread(),money,gMoney))
            gLock.release()
            time.sleep(1)




def main():
    for x in range(3):
        p = Producer(name="线程%d"%x)
        p.start()


    for x in range(5):
        c = Consumer(name="线程%d"%x)
        c.start()


if __name__ == '__main__':
    main()