"""
Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.
Мельник Д.В. 122А
Рекурсію я тут написав швидше ніж ітераційний алгоритм.Проте час виконання рекурсії частіше довший
По читабельності рекурсія зрозуміліша
"""
from datetime import datetime
import time

while True:
    def digit_root_iter(number):
        root = 0
        flag = False  # Прапорець
        while flag == False:
            for i in range(len(number)):  # Проходимось по цифрам числа і інтуємо їх, потім шукаєм суму цифр
                digit = int(number[i])
                root += digit
                if root >= 10 and i == len(number) - 1:  # Якщо сума цифр більше 10, то повертаємось на початок циклу
                    number = str(root)
                    root = 0
                elif root < 10 and i == len(number) - 1:  # Якщо сума цифр суми < 10,то міняємо прапорець та виходим з циклу
                    flag = True
                    print(root)


    def digit_sum(number):  # Шукаємо суму цифр
        if int(number)<10:  # Якщо число містить в собі лише 1 цифру,то повертаємо число
            return int(number)
        return int(number)%10 + digit_sum(int(number)//10)  # Рекурсивно знаходимо суму цифр числа


    def digit_root_recurs(number):
        if int(number) < 10:  # Якщо число містить в собі лише 1 цифру,то повертаємо число
            return int(number)
        return digit_root_recurs(digit_sum(int(number)))

    while True:
        try:
            number = input('Введіть число: ')  # Щоб не визначити окремо цифри числа ариф.операціями при ітераціях робимо стрний інпут
            int(number)
            if int(number) > 0:
                break
            else:
                print('Потрібно ввести натуральне число')
        except ValueError:
            print('Потрібно ввести число')
    start_time_iter = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    digit_root_iter(number)
    print(f'Iteration time: {datetime.now() - start_time_iter}')
    start_time_rec = datetime.now()
    time.sleep(1)  # Ставим відлік(1 секунду) на виконання програми, шоб вловити мікросекунди дейттаймом
    print(digit_root_recurs(number))
    print(f'Recursion time: {datetime.now() - start_time_rec}')
    print('Для виходу напишіть: exit')
    end = input('Cюди:')
    if end == 'exit':
        exit()
