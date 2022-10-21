# 带有参数的装饰器，其实就是定义了一个函数，让函数接收参数，在函数内部返回一个装饰器。
def return_decorator(flag):
    def decorator(func):
        def inner(a, b):
            if flag == "+":
                print("Add calculating....")
            elif flag == "-":
                print("Sub calculating...")
            func(a, b)

        return inner

    return decorator


@return_decorator("+")
# decorator = return_decorator("+"), @decorator => add_num = decorator(add_num)
def add_num(a, b):
    result = a + b
    print(result)


@return_decorator("-")
def sub_num(a, b):
    result = a - b
    print(result)


add_num(1, 2)
sub_num(1, 4)
