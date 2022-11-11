# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".


data = 'абвамтоат ваьамлв асывьлмо ьмслс абва мьшлмтшв а абв'
text = data.split()
indexes = []

i = len(text) - 1
while i >= 0:
    if 'абв' in text[i]:
        text.remove(text[i])
    i -= 1
print(*text)


# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

#---вариант игры с "интеллектуальным" ботом, первым ходит человек---

# candies = 2021
# max_turn = 28
# def Win_turn(num, max_turn):
#     return num % (max_turn + 1)
# first_turn = Win_turn(candies, max_turn)
# print(f'Для победы первому игроку необходимо взять {first_turn} конфет')
# while candies > 0:
#     first_player = int(input('Введите количество конфет от 1 до 28: '))
#     while first_player < 1 or first_player > 28:
#             first_player = int(input('Неверное количество! Введите количество конфет от 1 до 28: '))
#     candies -= first_player
#     if candies == 0:
#         print('Вы победили!')
#         break
#     elif candies >= max_turn + 1:
#         bot = Win_turn(candies, max_turn)
#         if bot == 0:
#             bot += 1
#     else:
#         bot = candies
#     print(f'Бот взял: {bot}')
#     candies -= bot
#     print(candies)
#     if candies == 0:
#         print('Победил бот!')


# 3. Создайте программу для игры в "Крестики-нолики".

#---to be completed later(---  


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример
# а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

with open('data_in.txt', 'r') as data:
    txt = data.readline()
print(txt)

count = 0
temp = txt[0]
out = ''
for i in txt:
    if i == temp:
        count += 1
    else:
        out += str(count)
        out += temp
        temp = i
        count = 1
out += str(count)
out += temp
print(out)

with open ('data_out.txt', 'w') as output:
    output.write(out)

count = ''
out_recovered = ''
for i in out:
    if i.isdigit():
        count += str(i)
    else:
        out_recovered += i*int(count)
        count = ''
print(out_recovered)