# 装饰器
# 就是给已有函数增加额外功能的函数，本质上就是一个闭包函数，它也是一个函数的嵌套。

# 不修改已有函数的源代码
# 不锈钢已有函数的调用方式
# 给已有函数增加额外的功能

# 定义装饰器
def decorator(func):
    # 如果闭包函数的参数有且只有一个并且是函数类型，那么这个闭包函数称为装饰器。
    print("decorator executing!")

    def inner():
        # 再内部函数里面对已有函数进行装饰
        print("Login succeeds!")
        func()

    return inner


# 装饰器的语法糖写法，@装饰器名称。
@decorator  # comment = decorator(comment) 装饰器语法糖对该代码进行了封装
def comment():
    print("Publishing!")


# 调用装饰器对已有函数进行装饰
# comment = decorator(comment)
# print("Login succeeds!")
comment()
