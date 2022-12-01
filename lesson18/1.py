from abc import abstractclassmethod


class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    @abstractclassmethod
    def say(self):
        pass


class Cat(Animal):
    def say_c(say):
        print("meow!")


class Dog(Animal):
    def say_d(say):
        print("woof!")
c = Cat("Barsik", "pink", "16")
d = Dog("Pes", "punk", "4")

print(f"{c.name}, {c.color}, {c.age}")
c.say_c()
print(f"{d.name}, {d.color}, {d.age}")
d.say_d()
