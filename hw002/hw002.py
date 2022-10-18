# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


num = input('Введите вещественное число: ')
sum = 0
for i in range(len(num)):
    if num[i].isdigit():
        sum += int(num[i])
print(sum)


# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input('Введите число: '))
temp = 1
list = []
for i in range(1, n+1):
    temp *= i
    list.append(temp)
print(list)


# Задайте список из n чисел последовательности (1 + 1/n)^n 
# и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} 
# Сумма 9.06


n = int(input('Введите число: '))

d = {i: round(((1 + 1/i)**i), 2) for i in range(1, n+1)}
print(d)
sum=0
for i in d.values():
    sum += i
print(f'Сумма: {sum}')


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


import random

n = int(input('Введите число: '))
list = []
for i in range(n):
    list.append(random.randint(-n, n))
print(list)

data = open('text.txt', encoding='utf-8')
positions = data.readlines()
data.close()
result = list[int(positions[0])-1] * list[int(positions[1])-1]
print(result)


# Реализуйте алгоритм перемешивания списка.


list = ['cat', 'dog', 1, 2, 3, 4, 5, 'gb']
print(list)
# random.shuffle(list)
# print(list)

import time

for i in range(len(list)):
    n = str(time.time())[-1]
    j = int(n)
    temp = list[i]
    if j < len(list):
        list[i] = list[j]
        list[j] = temp

print(list)