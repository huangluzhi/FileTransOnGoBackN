import threading
import time


def singleton(cls):
    instance = cls()

    def new_call(self):
        print('fuck')
        return instance

    def single_new(self):
        print('try create')
        return instance
    cls.__call__ = new_call
    cls.__new__ = single_new
    return cls

# 终于成功了，日了狗，python怎么什么jb类型都能返回，我TM装饰器返回了不对劲的东西他都不管的


@singleton
class Hive(object):
    x = 20

    def __init__(self):
        print('init here')
        time.sleep(2)
        # pass


print(Hive)
print(Hive())


def task(arg):
    obj = Hive()
    time.sleep(2)
    obj.x = obj.x + 1
    print(obj.x)
    print(obj)


for i in range(100):
    t = threading.Thread(target=task, args=[i, ])
    t.start()

print(Hive().x)
