# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите вещественное число: ')
num = list(map(int, filter(lambda x: x not in (',', '.'), num)))
print(sum(num))


# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'абвамтоат ваьамлв асывьлмо ьмслс абва мьшлмтшв а абваа авб абв'
cut = 'абв'
new_text = filter(lambda x: not cut in x, text.split())
print(*new_text)


# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as r
from functools import reduce


nums = [r(1, 20) for i in range(r(10, 20))]
print(nums)
def del_even(x):
    y = []
    for el in range(len(x)):
        if not el % 2:
            y.append(x[el])
    return y
print('На нечётных позициях элементы: ')
print(*del_even(nums))
sum_el = reduce((lambda x, y: x+y), del_even(nums))
print(f'Их сумма: {sum_el}')