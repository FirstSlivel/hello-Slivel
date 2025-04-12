print("☆" * 5 , " Игра Крестики-нолики для двоих! ", "☆" * 5)  # Название игры!

# Функция для создания и сброса игрового поля
def reset_game_board():
    return list(range(1, 10))

# Создаём функцию, отображающую игровое поле.
def create_a_board(gameboard):
    print("𝄖" * 10)  # Верхняя граница.
    for i in range(3):
        # Строки с клетками.
        print("|", gameboard[0 + i * 3], "|", gameboard[1 + i * 3], "|", gameboard[2 + i * 3], "|")
        print("𝄖" * 10)  # Нижняя граница.

# Создаём функцию выбора хода игрока.
def take_input(player_choice, game_board):
    valid = False
    # Создаём цикл проверки на ошибку.
    while not valid:
        player_answer = input("Куда поставим " + player_choice + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:  # Конкретика в обработке ошибки.
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            # Проверка клетки на занятость.
            if str(game_board[player_answer - 1]) not in "XO":
                # Записываем выбор игрока на игровом поле.
                game_board[player_answer - 1] = player_choice
                valid = True
                print("Ваш выбор принят! ")
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

# Создаём функцию проверки победы.
def check_win(board):
    win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_combo:
        if board[i[0]] == board[i[1]] == board[i[2]] != " ":
            return board[i[0]] # Возвращаем символ победителя.
    return False

# Основная функция игры
def play_game():
    game_board = reset_game_board()   # Сброс игрового поля
    game_counter = 0
    win = False

    while not win and game_counter < len(game_board):
        create_a_board(game_board)   # Отображаем текущее состояние игрового поля

        if game_counter % 2 == 0:
            take_input("X", game_board)   # Ход игрока X
        else:
            take_input("O", game_board)   # Ход игрока O

        game_counter += 1

        if game_counter > 4:   # Проверяем на победу после первых четырех ходов
            winner = check_win(game_board)
            if winner:   # Если есть победитель
                create_a_board(game_board)   # Отображаем финальное состояние игрового поля перед выводом результата
                print(f"Победитель: {winner}")
                win = True

            elif game_counter == len(game_board):   # Или проверяем на ничью (если все клетки заполнены)
                create_a_board(game_board)
                print("Ничья!")

# Запуск игры с возможностью повторной игры
while True:
    play_game()

    play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
    if play_again != 'да':
        break

input("Нажмите Enter для выхода!")