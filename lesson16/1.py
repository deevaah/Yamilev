class Cat:
    def __init__(self,name, color, age ):
       self.name = name
       self.color = color
       self.age = age
    def meow(self):
        print(self.name + ": MEEEEEOOOOWGIVEMEFOOOOD!")
    def purr(self):
        print(f"{self.name}: MRRRRROLOVEYOU!")
    def hiss(self):
        print(f"{self.name}: HSHSHSHSHHSWHOTHEFAREYOU!")
cat = Cat("SHARIKVLADIMIROVICH", "GOLYBOY", "24")
print("MY NAME IS",cat.name,"and my fur is", cat.color,"MY AGE IS", cat.age)
cat.meow()
cat.purr()
cat.hiss()