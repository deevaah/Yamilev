from time import sleep
import sys
a = 0

class Car:
    def __init__(self, color, mark, body, transmission, speed = 0):
        self.color = color
        self.mark = mark
        self.body = body
        self.speed = speed
        self.transmission = transmission

    def start(self):
        print("\nмашина начала движение")
        print("скорость: 10 km/h")
        self.speed = 10
    def stop(self):
        print("\nмашина остановилась")
        print('скорость: 0 km/h')
        self.speed = 0
    def turn(self, a):
        storona = input("в какую сторону поворот? направо/налево ")
        if storona == "налево":
            print("машина повернула налево")
            if a == 0:
                sys.exit("Ты повернул на встречку и разбился")
            if a == 1:
                sys.exit("Ты повернул не туда, и опоздал на работу, и стал бездомным")
        elif storona == "направо":
            print("машина повернула направо")

    def speed_up(self):
        self.speed += 50
        if self.body == 'Грузовик':
            if self.speed >= 60:
                self.speed = 60
                print('\nты нажал на газ!')
                print(f'Скорость превышена! разрешенная скорость 60км/ч. \nскорость: {self.speed} км/ч')
            else:
                print('\nты нажал на газ!')
                print(f'скорость машины {self.speed} км/ч')
        else:
            if self.speed >= 80:
                self.speed = 80
                print('\nты нажал на газ!')
                print(f'Скорость превышена! разрешенная скорость 80 км/ч. \nскорость:  {self.speed} км/ч')
            else:
                print('\nты нажал на газ!')
                print(f'скорость машины: {self.speed} км/ч')
    def speed_down(self, i=1):
        if self.speed == 0:
            print("\nскорость: 0 km/h")
        else:
            print("\nмашина замедляется")
            print(f"скорость: {self.speed - i} km/h")
            self.speed -= i
    def beep(self):
        print("биип")
car = Car("Серозеленый Металлик", "Лада", "Лифтбек", "Механика")
truck = Car("Красная", "Шакман", "Грузовик", "Автомат")
print(car.mark, car.color, car.body, car.transmission, "\n")
sleep(1)
car.start()
sleep(1)
car.turn(0)
sleep(1)
car.speed_up()
car.speed_up()
sleep(1)
print("Вас остановил полицейский.")
sleep(1)
car.stop()
sleep(1)
print("Полицейский: поаккуратнее со скоростью, молодой человек.")
