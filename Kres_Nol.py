# количество клеток
kol_klet = 3
kol_stolb = 4

# доска
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# рисуется игровое поле
def game_board():
    # Выводится игровое поле
    print('-' * 6 * kol_klet + '-')
    for i in range(kol_klet):
        print(('|' + ' ' + ' ' + ' ' * 3) * kol_stolb)
        print('|', '', board[i * 3], '', '|', '', board[1 + i * 3], '', '|', '', board[2 + i * 3], '', '|')
        print(('|' + ' ' + ' ' + ' ' * 3) * kol_stolb)
        print('-' * 6 * kol_klet + '-')

# Функция хода игроков
def game_step(index, char):
    if (index > 9 or index < 1 or board[index - 1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True

# Проверяется победы одного из игроков
def check_win():
    win = False
    win_combi = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),    # по горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),    # по вертикали
        (0, 4, 8), (2, 4, 6)                # по диагонали
    )
    for pos in win_combi:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win
# Запуск игры
def start_game():
    # текущий игрок
    players = 'X'
    # номер шага
    step = 1
    game_board()
    while (step < 10) and (check_win() == False):
        index = input('Ходит игрок ' + players + "\n" + 'Выход - (0)' + "\n" + 'Ведите номер клетки:')

        if (index == '0'):
            break

        # если получилось сделать шаг
        if (game_step(int(index), players)):
            print ('Удачный ход')
            # Смена игроков
            if (players == 'X'):
                players = 'O'
            else:
                players = 'X'

            game_board()
            # увеличивается номер хода
            step += 1
        else:
            print ('Неверный номер клетки! Повторите ещё!')

    if (step == 10):
        print ('Игра окончена. НИЧЬЯ!')
    elif check_win() != False:
        print('Выиграл игрок ' + str(check_win()))


print('Добро пожаловать в игру "Крестики-Нолики"!')
start_game()