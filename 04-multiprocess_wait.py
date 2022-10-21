import multiprocessing
import time


def task():
    # for i in range(10):
    while True:
        print("Executing....")
        time.sleep(0.2)


if __name__ == "__main__":
    sub_process = multiprocessing.Process(target=task)

    # 1.把子进程设置成为守护主进程，以后主进程退出子进程直接销毁。
    # sub_process.daemon = True

    sub_process.start()

    time.sleep(0.5)
    # 2. 退出主进程之前，先让子进程进行销毁。
    sub_process.terminate()
    print("over")
    # 主进程会等的子进程执行完成以后程序再退出。

    # 主进程退出，子进程销毁。两种方法：
    # 1. 让子进程设置成为守护主进程，主进程退出，子进程销毁，子进程依赖主进程。
    # 2. 让主进程退出之前先让子进程销毁。
