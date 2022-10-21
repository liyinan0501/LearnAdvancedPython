from ast import arg
import threading


def show_info(name, age):
    print("name: %s age: %d" % (name, age))


if __name__ == "__main__":
    # 以元祖方式传参，要保证元祖里面元素的顺序和函数的参数顺序一致。
    # sub_thread = threading.Thread(target=show_info, args=("Jack", 55))
    # sub_thread.start()

    # 以字典的方式传参，要保证字典里面的key和函数的参数名保持一致。
    sub_thread = threading.Thread(target=show_info, kwargs={"name": "Jack", "age": 22})
    sub_thread.start()
