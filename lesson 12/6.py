def factorial(num):
    rs = 1
    while num > 0:
        rs *= num
        num -= 1
    return rs


print(factorial(5))


def factorial(num):
    if num == 1:
        return 1
    rs = num * factorial(num - 1)
    return rs


print(factorial(5))
