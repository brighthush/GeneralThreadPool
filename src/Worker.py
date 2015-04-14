#coding=utf8
import threading
import Queue
import time

elements = ["bread", "rice", "water", "apple", "orange"]

queueLock = threading.Lock()
dataQueue = Queue.Queue()

queueLock.acquire()
for ele in elements:
    dataQueue.put(ele)
queueLock.release()

class Worker(threading.Thread):
    def __init__(self, threadName, workerQueue, func):
        super(Worker, self).__init__()
        self.threadName = threadName
        self.workerQueue = workerQueue
        self.workingEvent = threading.Event()
        self.doWorking = func
        self.args = None

    def setArgs(self, args):
        self.args = args

    def setWorking(self):
        self.workingEvent.set()

    def clearWorking(self):
        self.workingEvent.clear()

    def currentThread(self):
        return threading.currentThread()

    def getName(self):
        return self.threadName

    def run(self):
        while True:
            self.workingEvent.wait()
            if self.args == None:
                print '\t%s finished.' %(self.threadName)
                break
            self.doWorking(self.args)
            self.clearWorking()
            self.workerQueue.put(self.currentThread())

"""
            self.qLock.acquire()
            if self.q.empty():
                print "dataQueue is empty, ID[%s] is exited." %(self.threadID)
                self.qLock.release()
                break
            else:
                ele = self.q.get()
                print "threadID %d, consume %s" \
                        %(self.threadID, ele)
                self.qLock.release()
            time.sleep(1.0)

def main():
    global queueLock
    global dataQueue
    threads = []
    for i in range(3):
        consumer = Consumer(i, dataQueue, queueLock)
        threads.append(consumer)
    for thread in threads:
        print thread.threadID, thread.getName()
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
"""

