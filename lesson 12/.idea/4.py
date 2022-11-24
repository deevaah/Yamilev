def count():
    i = 0
    while i < 11:
        print(i)
        i += 1

count()

def count(i=0):
    if i == 10:
        print(i)
        return
    else:
        print(i)
        return count(i + 1)


count()
