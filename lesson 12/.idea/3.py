a = 0
def hello():
    lst = []

    while a == 0:
        name = input('Как тебя зовут?: ')
        if name not in lst:
            print("Привет,",name,", Рад знакомству!")
            lst.append(name)
            continue
        print("Привет,",name,)


hello()
