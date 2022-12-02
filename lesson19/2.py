class Queue:
    def __init__(self):
        self.inside = ["Леха", "Никита", "Вадим"]
    def __add__(self, other):
        self.inside.append(other)
    def __isub__(self, other):
        self.inside.pop(other)
        return self
    def __str__(self):
        return " => ".join(self.inside)
    def add(self):
        name = input("Кассир:Следующий!!")
        self.inside.append(name)
    def take_out(self):
        self.inside.pop(0)
a = Queue()
print(a)
a.add()
a.take_out()
print(a)
a.add()
a.take_out()
print(a)