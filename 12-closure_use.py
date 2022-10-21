# 外部函数接受姓名参数
def config_name(name):
    # 内部函数保存外部函数的参数，并且完成数据显示组成。
    def inner(msg):
        print(f"{name}: {msg}")

    print(id(inner))
    # 外部函数要返回内部函数
    return inner


tom = config_name("Tom")
jerry = config_name("Jerry")

tom("come on")
jerry("!!")
