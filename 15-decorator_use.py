import time
from unittest import result


def decorator(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()

        result = end - begin
        print("Cost: ", result)

    return inner


@decorator  # work = decorator(work)  => work = inner
def work():
    for i in range(10000):
        print(i)


work()
