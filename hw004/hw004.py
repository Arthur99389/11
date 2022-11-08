# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...


pi = 0
num = int(input('Задайте количество знаков после запятой для вычисления числа π: '))
for n in range(num):
    pi += (1 / (16 ** n)) * (4 / (8 * n + 1) - 2 / (8 * n + 4) - 1 / (8 * n + 5) - 1 / (8 * n + 6))
print(pi * 10 ** num // 1 / 10 ** num)


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


N = int(input('Введите натуральное число: '))
multipliers = []
tempN = N
count = 2
while count <= N:
    if tempN % count == 0:
        multipliers.append(count)
        tempN /= count
    else: count += 1
            
print(f'Простые множители введённого числа: {multipliers}')


# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


import random

random_list = [random.randint(1, 20) for i in range(random.randint(10, 30))]
print(random_list)
uniq_list = [i for i in set(random_list) if random_list.count(i) == 1]
print(uniq_list)


# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#  Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


k = int(input('Введите натуральную степень k: '))
pol = []

def rnd(): 
    return random.randint(0, 100)

for i in range(k, 1, -1):
    a = rnd()
    if a:
        pol.append(f'{a}x^{i}')

a = rnd()
if a:
    pol.append(f'{a}x')

a = rnd()
if a:
    pol.append(str(a))

pol_fin = ' + ' .join(pol) + ' = 0'
print(pol_fin)

with open('polynom.txt', 'w') as data:
    data.write(pol_fin)


# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.