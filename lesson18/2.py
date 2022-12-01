class Father:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Child(Father):
    def __init__(self, patronim):
        super().__init__("Hello", "World" )
        self.patronim = patronim
kiddo = Child("Worldowich")
print(kiddo.surname, kiddo.name, kiddo.patronim)