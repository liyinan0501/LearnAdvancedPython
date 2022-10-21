import threading
import time

g_list = []


def add_data():
    for i in range(3):
        g_list.append(i)
        print("add: ", i)
        time.sleep(0.2)
    print("Adding completed!", g_list)


def read_data():
    print("Read: ", g_list)


if __name__ == "__main__":
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    add_thread.start()

    # time.sleep(1)
    # 当前线程等待添加数据的子线程执行完成以后，其余的代码再继续执行。
    add_thread.join()
    read_thread.start()
