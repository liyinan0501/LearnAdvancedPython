import threading

lock = threading.Lock()


def get_value(index):

    lock.acquire()
    my_list = [1, 4, 6]

    if index >= len(my_list):
        print("Index out range: ", index)
        # 取值不成功，也需要释放互斥锁，不要影响后面的线程取值。
        lock.release()
        return

    value = my_list[index]
    print("value: ", value)
    lock.release()


if __name__ == "__main__":
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()
