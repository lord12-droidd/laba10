"""Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну.
Мельник Д.В. 122А
По швидкості написання ітераційний алгоритм швидше, по швидкості виконання ітераціїї частіше всього швидші
По читабельності ітераціїї кращі
"""
import time
from datetime import datetime

# щоб перевести число, потрібно його цикліно ділити на 16 і остачі скласти у зворотньому порядку

while True:
    def func_iter(number,hex_number):
        while number >= 0:
            ostacha = number % 16
            number = number // 16
            if ostacha in range(10, 16):  # Якщо остача від 10 до 15 то міняємо її на букву і конкатенуємо із стрічкою
                hex_number += letter_part[ostacha]
            else:
                hex_number += str(ostacha)  # Якщо ні, то просто конкатенуємо
            if number == 0:
                ostacha = number % 16
                hex_number += str(ostacha)
                break
        hex_number = hex_number[::-1]
        print(hex_number.strip(hex_number[0]))

    def func_rec(number1):
        if number1 >= 16:  # перевірка чи число, або остача від ділення менше 16, щоб завершити функцію
            if number1 % 16 in range(10, 16):  # якщо остача від ділення в межах від 10 до 15, то потрібно перевести число в букву
                return func_rec(number1 // 16) + letter_part[number1 % 16]
            else:  # якщо остача від ділення менше 10, то переводимо число в стрічку і додаємо до результату
                return func_rec(number1 // 16) + str(number1 % 16)
        else:  # якщо остача від ділення менше 16, то додаємо останній елемент до результату
            if number1 in range(10, 16):
                return letter_part[number1 % 16]
            else:
                return str(number1 % 16)

    while True:
        try:
            number = int(input('Введіть число: '))
            break
        except ValueError:
            print("Потрібно ввести число")
    number1 = number
    hex_number = ''
    letter_part = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    start_time_iter = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    func_iter(number,hex_number)
    print(f'Iteration time: {datetime.now() - start_time_iter}')
    start_time_rec = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    print(func_rec(number1))
    print(f'Recursion time: {datetime.now() - start_time_rec}')
    print('Для виходу напишіть: exit')
    end = input('Cюди:')
    if end == 'exit':
        exit()