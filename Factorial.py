"""Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.
Мельник Д.В. 122А
Я розробляв цю програму однаково по часу , що для рекурсії, що для ітерації
По часу виконання частіше рекурсія виконується довше ніж ітерації
По читабельності мені зрозуміліший ітераційний алгоритм
"""

from datetime import datetime
import time

while True:
    def factorial_rec(number):
        if number == 1 or number == 0:
            return 1
        return factorial_rec(number - 1) * number



    def factorial_iter():
        mult = 1
        for i in range(1, number + 1):
            mult = mult * i
        print(mult)
    while True:
        try:
            number = int(input('Enter the number: '))
            if number >= 0:
                break
            else:
                print('Факторіал існує лише для натуральних чисел')
        except ValueError:
            print('Потрібно ввести натуральне число')
    start_time_rec = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    print(factorial_rec(number))
    print(f'Recursion time:{datetime.now() - start_time_rec}')
    start_time_iter = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    factorial_iter()
    print(f'Iteration time: {datetime.now() - start_time_iter}')
    print('Для виходу напишіть: exit')
    end = input('Cюди:')
    if end == 'exit':
        exit()
