"""Cформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників крім 1 та самого себе.
Мельник Д.В. 122А
Рекурсії працюють швидше, по читабельності однакові, Написав швидше ітераційний алгоритм.
"""

import math
import time
from datetime import datetime

while True:
    def common_iter(n):
        i = 2
        j = 0  # Прапорець
        while i**2 <= n and j != 1:
            if n%i == 0:  # Якщо остача від ділення на число і буде 0, то число складне
                j = 1
            i += 1  # Якщо ні, то число просте
        if j == 1:
            print("Складне")
        else:
            print("Просте")


    def commom_recurs(n, i):
        j = 2  # Врахували що просте число ділиться на 1 та на саме себе
        if (n % i == 0 and i < 10) or n % math.sqrt(n) == 0:  # Ділимо наше число на цифри а потім перевіряюмо квадрати простих чисел
            if i != n:
                j += 1
            if j > 2:  # Якщо в числе більше ніж 2 дільника, то складне
                return (print("Складне"))
            else:  # Інакше просте
                return (print("Просте"))
        elif i >= 10 and j <= 2:
            return (print("Просте"))
        else:
            return (commom_recurs(n, i + 1))


    while True:
        try:
            n = int(input('Введіть число: '))  # Перевірки
            if n <= 0:
                print('Число повинне бути натуральним')
            elif n == 1:
                print('Не просте і не складне')
            else:
                break
        except ValueError:
            print('Повинно бути введено число')
    i = 2
    start_time_iter = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    common_iter(n)
    print(f'Iteration time: {datetime.now() - start_time_iter}')
    start_time_rec = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    commom_recurs(n, i)
    print(f'Recursion time: {datetime.now() - start_time_rec}')
    print('Для виходу напишіть: exit')
    end = input('Cюди:')
    if end == 'exit':
        exit()
