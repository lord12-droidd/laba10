"""
Сформувати функцію для введення з клавіатури послідовності чисел і виведення
її на екран у зворотному порядку (завершаючий символ послідовності – крапка)
Мельник Д.В. 122А
Рекурсії працюють довше, по часу написанню алгоритмів однаково, по читабельності ітераційний краще
"""

import time
from datetime import datetime

while True:
    def reverse_iter(j):
        for i in range(len(numbers_list_iter)//2):
            j += 1
            numbers_list_iter[i],numbers_list_iter[-j] = numbers_list_iter[-j],numbers_list_iter[i]  # Міняємо місцями перший елемент з останнім
            if '.' not in numbers_list_iter[-1]:  # Додаємо до останнього елементу крапку
                numbers_list_iter[-1]=numbers_list_iter[-1]+'.'
        print(*numbers_list_iter)


    def reverse_recursive(numbers_list_recurs):
        if not numbers_list_recurs:
            return numbers_list_recurs
        return [numbers_list_recurs.pop()] + reverse_recursive(numbers_list_recurs)


    while True:
        try:
            numbers = input().replace('.', '').split()  # Вводимо послідовність, перевірка на входження лише чисел у неї
            for i in numbers:
                int(i)
            break
        except ValueError:
            print('В послідовності повинні бути лише числа')
    numbers_list_iter = [i for i in numbers]  # Два однакових масиви для кожної функції, бо якщо працювати з одним і тим самим,
    numbers_list_recurs = [i for i in numbers]  # то він буде у одній із функцій повертатись в початковий варіант
    j = 0
    m = 0
    start_time_iter = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    reverse_iter(j)
    print(f'Iteration time: {datetime.now() - start_time_iter}')
    start_time_rec = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    print(*reverse_recursive(numbers_list_recurs),end='.')
    print(f'\nRecursion time: {datetime.now() - start_time_rec}',end='\n')
    print('Для виходу напишіть: exit')
    end = input('Cюди:')
    if end == 'exit':
        exit()