#coding=utf8
import threading
import Queue
from Worker import Worker
import time

class Manager(threading.Thread):
    taskQueue = Queue.Queue()
    workerQueue = Queue.Queue()
    workerNum = 5
    def __init__(self, workerNum=5):
        super(Manager, self).__init__()
        self.workerNum = workerNum
        for i in range(self.workerNum):
            worker = Worker('worker-thread[%d]' %(i), self.workerQueue, func)
            self.workerQueue.put(worker)
            worker.start()

    def addTask(self, task):
        self.taskQueue.put(task)

    def run(self):
        while True:
            if not self.taskQueue.empty():
                args = self.taskQueue.get()
                thread = self.workerQueue.get()
                thread.setArgs(args)
                thread.setWorking()
            else:
                print 'Manager sleep 1 sec ...'
                time.sleep(1)


def func(args):
    for arg in args:
        print '%s func arg = %s' \
                %(threading.currentThread().getName(), arg)

def main():
    workerNum = 5
    manager = Manager()
    manager.start()
    for i in range(50):
        args = (i, )
        manager.addTask(args)
        if i%10 == 0:
            print 'main sleep 2 secs.'
            time.sleep(2)
    for i in range(workerNum):
        manager.addTask(None)

if __name__ == '__main__':
    main()

