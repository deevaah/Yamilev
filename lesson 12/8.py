from random import randint


def quizz(num=randint(0, 100), n=0):
  if n != 10:
    user_num = int(input(f'Попытка #{n + 1}. Введите число:'))
    if user_num == num:
      return print(f'Вы угадали. Загаданное число {user_num}')
    elif user_num > num:
      print(f'Меньше {user_num}')
    else:
      print(f'Больше {user_num}')
    return quizz(num, n + 1)
  return print(f'Вы проиграли! Загаданное число было: {num}')


quizz()