def make_p(func):
    print("make_p")

    def inner():
        result = "<p>" + func() + "</p>"
        return result

    return inner


def make_div(func):
    print("make_div")

    def inner():
        result = "<div>" + func() + "</div>"
        return result

    return inner


# 多个装饰器过程：由内到外的一个装饰过程。
# 原理剖析：conent = make_div(make_p(content))
# 分布拆解：conent = make_p(content)， 内部装饰器完成 conent = make_p.inner
# content = make_div(make_p.inner)
@make_div
@make_p
def content():
    return "Life is short"


result = content()
print(result)
