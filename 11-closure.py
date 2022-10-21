# 闭包
# 1. 函数嵌套
# 2. 内部函数使用外部函数的变量
# 3. 外部函数返回了内部函数
# 作用
# 闭包可以保存外部函数内的变量，不会随着外部函数调用完而销毁。


def fn_out():
    num1 = 10  # 这个变量不会丢失

    def fn_inner(num2):
        result = num1 + num2
        print("Result:", result)

    return fn_inner


# 获取闭包对象
# new_fn 就是闭包
new_fn = fn_out()
# new_fn = fun_inner
new_fn(1)
new_fn(10)
