def calculator():
    number1 = int(input('Введите число:'))
    sign = input(':')
    number2 = int(input('Введите число:'))

    if sign == '+':
        return number1 + number2
    elif sign == '-':
        return number1 - number2
    elif sign == '*':
        return number1 * number2
    elif sign == '/' and b != 0:
        return number1 / number2
    else:
        print('Ошибка')

print(calculator())
