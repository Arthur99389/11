# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

rand_list = [random.randint(1, 10) for i in range(random.randint(10, 20))]
print(rand_list)
sum = 0
for i in range(1, len(rand_list), 2):
    sum += rand_list[i]
print(f'Сумма элементов с нечётными индексами: {sum}')


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


rand_list = [random.randint(1, 10) for i in range(random.randint(5, 10))]
print(rand_list)

list_mult = []

for i in range(int(len(rand_list)//2 + len(rand_list)%2)):
    list_mult.append(rand_list[i]*(rand_list[len(rand_list)-1-i]))
print(list_mult)


# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


rand_list = [round(random.uniform(1, 10), 2) for i in range(random.randint(5, 10))]
print(rand_list)
list_after_dot = []
for i in range(len(rand_list)):
    list_after_dot.append(round((rand_list[i]%1), 2))
print(f'Разница между максимальным ({max(list_after_dot)}) и минимальным ({min(list_after_dot)}) \
значениями дробной части элементов: {round((max(list_after_dot) - min(list_after_dot)), 2)}')


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


n = int(input('Введите десятичное число для перевода в двоичное: '))

doubled_n = ''

while n//2 >= 1:
    doubled_n += str(n%2)
    n = n//2
    if n == 1:
        doubled_n += '1'
print(''.join(reversed(doubled_n)))


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]
# F−1 = 1,
# F−2 = -1
# F{n}=F{n+2}-F{n+1}


k = int(input('Введите число: '))

def Fib(n):
    while n >= 0:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Fib(n-1) + Fib(n-2)

list_fib = []

for i in range(k+1):
    list_fib.append(Fib(i))

for i in range(1, len(list_fib)):
    if i % 2 == 0:
        list_fib.insert(0, -(Fib(i)))
    else:
        list_fib.insert(0, Fib(i))
print(list_fib)