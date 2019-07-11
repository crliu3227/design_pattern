import threading
import time


# 抽象实例
class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance


# 总线
class Bus(Singleton):
    lock = threading.RLock()

    def send(self, data):
        with self.lock:
            time.sleep(3)
            print("Sending Signal Data %s" % data)


# 发送信号的线程
class SendThread(threading.Thread):
    def __init__(self, name, bus):
        super(SendThread, self).__init__()
        self.name = name
        self.bus = bus

    def run(self):
        self.bus.send(self.name)


if __name__ == "__main__":
    sendthread = []
    bus = Bus()

    thread1 = SendThread('1', bus)
    thread2 = SendThread('2', bus)
    thread3 = SendThread('3', bus)

    sendthread.append(thread1)
    sendthread.append(thread2)
    sendthread.append(thread3)

    for t in sendthread:
        t.start()

    for t in sendthread:
        t.join()
