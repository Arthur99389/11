def Print_array(array):
    for i in range(len(array)):
        print(array[i])

def Check_winner(array):
    for x in range(len(array)):                     # проверка строк
        if array[x] == [player]*len(array):
            print(f'Победил Игрок {player}!')
            exit()
    for x in range(len(array)):                     # проверка колонок
        col = []
        for y in range(len(array)):
            col.append(array[y][x])
        if col == [player]*len(array):
            print(f'Победил Игрок {player}!')
            exit()
    cross1=[array[0][0],array[1][1],array[2][2]]      # проверка диагоналей
    cross2=[array[0][2],array[1][1],array[2][0]]
    if cross1 == [player]*len(array):
        print(f'Победил Игрок {player}!')
        exit()
    if cross2 == [player]*len(array):
        print(f'Победил Игрок {player}!')
        exit()

board = [[0,0,0],[0,0,0],[0,0,0]]
Print_array(board)

player = 1
for x in range(len(board)):
    for y in range(len(board)):
       row = int(input(f'Игрок {player}, введи строку: '))-1
       column = int(input(f'Игрок {player}, введи колонку: '))-1
       if board[row][column] == 0:
           board[row][column] = player
           Print_array(board)
           Check_winner(board)
           if player == 1: player = 2
           else: player = 1
       else:
            print('Эта клетка занята.')
print('Ничья.')