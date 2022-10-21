import multiprocessing
from multiprocessing.util import sub_debug


def show_info(name, age):
    print(name, age)


# 有一个参数因为是元组，需要加点,("Jack",)
# sub_process = multiprocessing.Process(target=show_info, args=("Jack",))
# sub_process = multiprocessing.Process(target=show_info, args=("Jack", 20))

# 以字典方式传参，字典里的key要和函数里的参数名保持一致，没有顺序要求。
# sub_process = multiprocessing.Process(
#     target=show_info, kwargs={"age": 20, "name": "jack"}
# )

# 位置传参和关键字传参混合使用
sub_process = multiprocessing.Process(
    target=show_info, args=("Jack",), kwargs={"age": 20}
)

sub_process.start()
