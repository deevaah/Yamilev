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

    def speed_up(self, i=1):
        print("\nты нажали на газ")
        print(f"\nскорость: {self.speed + i} km/h")
        self.speed += i
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
car.speed_up(120)
sleep(1)
print("Вас остановил полицейский.")
sleep(1)
car.stop()
sleep(1)
print("Полицейский: поаккуратнее со скоростью, молодой человек.")
sleep(1)
print("Выберите ответ")
sleep(1)
print("1-" "Дружище, я сын депутата", "2-" "Простите пожалуйста, я больше так не буду")
anwser = int(input("Введите:"))
if anwser == 1:
    print("Вас отпустили.")
elif anwser == 2:
    print("Вам выписали штраф.")
    print("Добавлен штраф:2000р")
sleep(1)
car.start()
sleep(1)
car.speed_up(60)
sleep(1)
car.speed_down(20)
sleep(1)
car.turn(1)

print("Ты приехал на работу!")
sleep(1)
print("Приступить к ней?")
print("1-да, 2-нет")
anwser1 = int(input("Введите:"))
if anwser1 == 2:
    sys.exit("Ты прогулял работу, тебя уволили, у тебя не хватило денег, и ты стал бездомным")
print("Ты на работе!")
print("Садишься в рабочую машину...")
sleep(4)
print("\n", truck.mark, truck.color, truck.body, truck.transmission, "\n")
sleep(1)
truck.start()
sleep(1)
truck.speed_up(20)
truck.speed_down(10)
sleep(1)
truck.turn(2)
sleep(1)
truck.speed_up(30)
sleep(1)
truck.speed_down(20)
sleep(1)
print("К вам на встречку выехала машина.")
sleep(2)
print("грузовик сделал " , end = " ")
truck.beep()
print("Вы врезались")