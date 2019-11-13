#-*-coding:utf-8-*-


import time
import threading
import random


'''
Condition()用法
'''


gMoney = 1000
gCondition = threading.Condition()
gTotalTimes = 10
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTotalTimes
        global gTimes
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            if gTimes >= gTotalTimes:
                gCondition.release()
                break
            gMoney += money
            print("%s线程生产了%d元钱，剩余%d元钱"%(threading.current_thread(),money,gMoney))
            gTimes += 1
            print(gTimes)
            gCondition.notify_all()
            gCondition.release()
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        # global gTotalTimes
        # global gTimes
        while True:
            money = random.randint(300,1000)
            gCondition.acquire()
            while gMoney < money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return
                print("%s准备消费%d元钱，剩余%d元钱，不足！"%(threading.current_thread(),money,gMoney))
                gCondition.wait()
            gMoney -= money
            print("%s消费了%d元钱，剩余%d元钱"%(threading.current_thread(),money,gMoney))
            gCondition.release()
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