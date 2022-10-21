# 1. 导入进程包。
import multiprocessing
import time
import os


def dance():
    dance_process_id = os.getpid()
    print("dance_process_id: ", dance_process_id, multiprocessing.current_process())
    # 获取父进程编号
    dance_process_parent_id = os.getppid()
    print("dance_process_parent_id: ", dance_process_parent_id)

    for i in range(3):
        print("Dancing...")
        time.sleep(0.2)
        # 根据进程编号强制杀死指定进程
        os.kill(dance_process_id, 9)


def sing():
    sing_process_id = os.getpid()
    print("sing_process_id: ", sing_process_id, multiprocessing.current_process())

    sing_process_parent_id = os.getppid()
    print("sing_process_parent_id: ", sing_process_parent_id)

    for i in range(3):
        print("Singing...")
        time.sleep(0.2)


# 获取当前（主）进程编号
main_process_id = os.getpid()
# 获取当前进程对象，查看当前代码是由哪个进程执行的：multiprocessing.current_process()
print("main_process_id: ", main_process_id, multiprocessing.current_process())

# 2. 因为默认有一个进程，自己手动创建的进程为子进程。
dance_process = multiprocessing.Process(target=dance)
print("dance_process: ", dance_process)
sing_process = multiprocessing.Process(target=sing)
print("sing_process: ", sing_process)
# 3. 启动进程，执行对应的任务。
dance_process.start()
sing_process.start()
# 进程执行是无序的，具体哪个进程先执行是由操作系统调度决定的。
