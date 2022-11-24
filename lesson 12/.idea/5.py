def fib():
    lst = [0, 1]
    i = 1

    while True:
        a = lst[i]
        b = lst[i - 1]
        c = a + b
        if c >= 100:
            break
        lst.append(c)
        i += 1
    return lst

print(fib())

def fibonacci():
    lst = [0]
    x1 = x2 = 1
    lst.append(x1)
    lst.append(x2)
    while x1 + x2 < 100:
        x1, x2 = x2, x1 + x2
        lst.append(x2)
    return lst

print(fibonacci())

def fibonacci(lst=[0, 1]):
    i = len(lst)
    b = lst[i - 1]
    a = lst[i - 2]
    c = a + b
    if c >= 100:
        return
    lst.append(c)
    fibonacci(lst)
    return lst

print(fibonacci())
