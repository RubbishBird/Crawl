#-*-coding:utf-8-*-

import threading
import time

# class CodingThread(threading.Thread):
#     def run(self):
#         for x in range(0, 3):
#             print("正在写代码%s" % threading.current_thread())
#             time.sleep(1)
#
#
# class DrawingThread(threading.Thread):
#     def run(self):
#         for x in range(0, 3):
#             print("正在画画%s" % threading.current_thread())
#             time.sleep(1)
#
# def main():
#     t1 = CodingThread()
#     t2 = DrawingThread()
#
#     t1.start()
#     t2.start()

# if __name__ == '__main__':
#     main()
VALUE = 0

GLock = threading.Lock()

def thread():
    global VALUE
    # GLock.acquire()
    for x in range(1000000):
        VALUE +=1
    # GLock.release()
    print('value:%s'%VALUE)

def main():
    for x in range(0,2):
        t1 = threading.Thread(target=thread)
        t1.start()

if __name__ == '__main__':
    main()