#coding=utf8
import threading
import time

def func(event):
    print '%s waiting event ...' %(threading.currentThread().getName())
    event.wait()
    print '%s event arried.' %(threading.currentThread().getName())

def main():
    event = threading.Event()
    t1 = threading.Thread(target=func, args=(event, ))
    t2 = threading.Thread(target=func, args=(event, ))
    t1.start()
    t2.start()

    time.sleep(2)
    print 'set event ...'
    event.set()

if __name__ == '__main__':
    main()

