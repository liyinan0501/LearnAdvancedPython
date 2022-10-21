def fn_out():
    num1 = 10

    def fn_inner():
        # 修改外部数据变量
        nonlocal num1
        num1 = 20

        result = num1 + 10
        print(result)

    print("Original: ", num1)
    fn_inner()
    print("After", num1)

    return fn_inner


new_fn = fn_out()
new_fn()
