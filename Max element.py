"""Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Мельник Д.В. 122А
Ітерації працюють швидше, рекурсивний алгоритм писати швидше,по читабельності впринципі однаково
"""
import time
from datetime import datetime

import numpy as np

while True:
    def index_max_element_iter():
        i = 0
        while i < len(massive) and massive[i] != max(massive):  # Поки ми не дійшли кінця списку та поки ми не знайдемо шукане число
            i += 1
        else:
            print(f"Максимальний елемент {max(massive)} знайдений на індексі {i}")  # і+1 щоб позиція була як лічба у нат.числах


    def index_max_element_recursion(m):
        if m < len(massive) and massive[m] != max(massive):  # Рекурсивний алгоритм
            return index_max_element_recursion(m + 1)
        return m


    m = 0
    massive = []  # Заводимо пустий список щоб потім визначити у ньому максимальний елемент
    while True:  # Перевірка на те щоб користувач ввів число та число було 1<=n<=5
        try:
            n = int(input('Введіть число n: '))
            if 1 <= n <= 5:
                break
            else:
                print("n повинно бути 1<=n<=5 ")
        except ValueError:
            print("n повинно бути числом")
    a = np.zeros((n, n), dtype=int)  # Ініціалізовуємо масив
    while True:
        try:
            for i in range(n):  # Заповнюємо вручну
                for j in range(n):
                    a[i, j] = int(input(f'A[{i},{j}]= '))
                    massive.append(a[i, j])
            break
        except ValueError:
            massive.clear()
            print("Масив має складатись лише з чисел")
    print(a)  # Виводимо введений масив
    start_time_iter = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    index_max_element_iter()
    print(f'Iteration time: {datetime.now() - start_time_iter}')
    start_time_rec = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    print(f'Максимальний елемент {max(massive)} знайдений на індексі {index_max_element_recursion(m)}')
    print(f'Recursion time: {datetime.now() - start_time_rec}')
    print('Для виходу напишіть: exit')
    end = input('Cюди:')
    if end == 'exit':
        exit()