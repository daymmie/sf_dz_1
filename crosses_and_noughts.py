N = 3
M = 3
crosses = 'x'
noughts = 'o'
space = '-'
win_combination = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]

A = []
for i in range(N):
    A.append([0] * M)

for i in range(N):
    for j in range(M):
        A[i][j] = space


def show_result():
    for i in A:
        for j in i:
            print(j, end=' ')
        print()
    return '____________________'

print("Правила игры: \n Один из игроков играет «крестиками», второй — «ноликами»."
      " \n Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики)."
      " \n Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает."
      " \n Первый ход делает игрок, ставящий крестики.")
print()
input("Нажмите Enter, чтобы продолжить:")
print()
print(" Воспользуйтесь цифрами на numpad (от 1 до 9). \n "
      "После того, как решили на какую клетку ходить нажмите Enter.")
print()
input("Нажмите Enter, чтобы продолжить:")
print('____________________')
print(show_result())


def turn_crosses(num_crosses):
    if num_crosses <= 3:
        for i in range(N):
            for j in range(M):
                A[2][num_crosses - 1] = crosses
    elif 3 < num_crosses <= 6:
        for i in range(N):
            for j in range(M):
                A[1][num_crosses - 4] = crosses
    elif 6 < num_crosses <= 9:
        for i in range(N):
            for j in range(M):
                A[0][num_crosses - 7] = crosses
    return '____________________'


def turn_noughts(num_noughts):
    if num_noughts <= 3:
        for i in range(N):
            for j in range(M):
                A[2][num_noughts - 1] = noughts
    elif 3 < num_noughts <= 6:
        for i in range(N):
            for j in range(M):
                A[1][num_noughts - 4] = noughts
    elif 6 < num_noughts <= 9:
        for i in range(N):
            for j in range(M):
                A[0][num_noughts - 7] = noughts
    return '____________________'

for a in range(1, 10):
    if a % 2 == 0:
        num_noughts = int(input('Ход игрока за нолики: '))
        print(turn_noughts(num_noughts))
        print(show_result())
    elif a % 1 == 0:
        num_crosses = int(input('Ход игрока за крестики: '))
        print(turn_crosses(num_crosses))
        print(show_result())
        for i in win_combination:
            symbols = []
            for j in i:
                symbols.append(A[j[0]][j[1]])
            if symbols == ['x', 'x', 'x']:
                print('Победа крестиков')
                input('Нажмите Enter, чтобы завершить игру')
                exit('Победа крестиков')
            elif symbols == ['o', 'o', 'o']:
                print('Победа ноликов')
                input('Нажмите Enter, чтобы завершить игру')
                exit('Победа ноликов')
    elif a == 9:
        break
else:
    print('Ничья')

