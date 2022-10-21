import threading

g_num = 0

# 创建互斥锁，Lock是一个函数，通过调用函数可以创建一个互斥锁。
lock = threading.Lock()


def task1():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1

    print("task1: ", g_num)
    # 释放锁
    lock.release()


def task2():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1

    print("task2: ", g_num)
    # 释放锁
    lock.release()


if __name__ == "__main__":
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    # first_thread.join()
    second_thread.start()

    # 保证同时一时刻只能有一个线程去操作代码，能够保证全局变量数据没有问题。
