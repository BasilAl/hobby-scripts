import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))
        time.sleep(1)
        print("{} finished!".format(self.getName()))

if __name__ == '__main__':
    for x in range(4):
        mythread = MyThread(name = f"Thread-{x+1}")
        mythread.start()
        time.sleep(.9)
