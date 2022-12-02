class Batary():
    def __init__(self):
        self.capacity = []
        self.max_charge = 5

    def __str__(self):
        return '[' + ''.join(self.capacity) +']'

    def charge(self):
        if len(self.capacity) >= self.max_charge:
            print("заряжено!")
        else:
            self.capacity.append(')')

    def discharge(self):
        self.capacity.pop(0)

bat = Batary()
bat.charge()
