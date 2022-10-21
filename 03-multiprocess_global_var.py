from ast import main
import multiprocessing
import time

g_list = []


def add_data():
    for i in range(3):
        # 因为列表是可变类型，可以在原有内存上修改数据，并且修改后内存地址不变。
        # 所以不需要加 global 关键字
        # 加上global 表示声明要修改全局变量的内存地址
        g_list.append(i)
        print("add: ", i)
        time.sleep(0.2)

    print("Add completed: ", g_list)


def read_data():
    print("read: ", g_list)


# 提示：
# 对于linux和mac主进程执行的代码不会全程拷贝，但是windows系统来说主进程代码也会进行拷贝
# 对于window来说创建子进程的代码如果进行拷贝执行相当于递归无限制进行创建子进程，回报错。
# 解决windows递归创建子进程的问题，通过判断是否是主模块来解决。
if __name__ == "__main__":
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    add_process.start()
    # 当前进程(主进程)等待添加数据的进程执行完成后再往下执行。
    add_process.join()
    print("main: ", g_list)
    read_process.start()

    # 进程之间不共享全局变量。
