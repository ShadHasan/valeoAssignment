from time import sleep


def fib(_iter):
    first = 1
    print("Sequence: {}".format(first))
    second = 1
    for i in range(_iter):
        print("Fib {} Sequence: {}".format(i, second))
        temp = first + second
        first = second
        second = temp
        sleep(1)


def even(_iter):
    first = 0
    for i in range(_iter):
        print("Even {} sequence = {}".format(i, first))
        first = first + 2
        sleep(1)
