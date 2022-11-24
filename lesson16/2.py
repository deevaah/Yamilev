class Good:
    def __init__(self, price, weight):
        self.cost = None
        self.price = price
        self.weight = weight

    def calcul(self):
        self.cost = self.price * self.weight


#pear('pear', price = 120, weight = 0.8)
#apple('apple', price = 100, weight = 1.5)
apple = Good(price=120, weight=float(input("Сколько яблоко весит?")))
pear = Good(price=100, weight=float(input("Сколько груша весит?")))
apple.calcul()
pear.calcul()
print(f"стоимость яблок {apple.cost}")
print(f"стоимость груш {pear.cost}")
