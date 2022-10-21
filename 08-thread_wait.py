from re import sub
import threading
import time


def task():
    while True:
        print("executing....")
        time.sleep(0.3)


if __name__ == "__main__":
    # daemon = Ture 表示创建的子线程守护主线程，主线程退出，子线程销毁。
    # sub_thread = threading.Thread(target=task, daemon=True)
    sub_thread = threading.Thread(target=task)
    sub_thread.setDaemon(True)

    sub_thread.start()
    time.sleep(1)
    print("over")
