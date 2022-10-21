class MyDecorator(object):
    def __init__(self, func) -> None:
        self.__func = func

    # 实现 __call__这个方法，让对象变成可调用对象，可调用对象能够像函数使用
    def __call__(self, *args, **kwargs):
        # 对已有函数进行封装
        print("after")
        self.__func()


@MyDecorator  # @MyDecorator => show = MyDecorator(show)
def show():
    print("work!")


# 没有call方法 show() 报错 is not callable
show()
# 如果func不变成私有的__func，在外面执行show.func可以访问到func。

# 查看类有哪些方法
print(dir(MyDecorator))
