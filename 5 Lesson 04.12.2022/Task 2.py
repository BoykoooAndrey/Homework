import random
candies = 100
motion = 1
number_of_players = input("Введите количество игроков 1 или 2:")

while not (number_of_players in ['1', '2']):
    number_of_players = input("Введите количество игроков 1 или 2:")
number_of_players = int(number_of_players)

if number_of_players == 1:

    difficulty_level = input("Введите уровень сложности 1 или 2:")
    while not (difficulty_level in ['1', '2']):
        difficulty_level = input("Введите уровень сложности 1 или 2:")
    difficulty_level = int(difficulty_level)

    name_player1 = str('Computer')
    name_player2 = str(input("Введите ваше имя:"))

    whose_move = input("Кто ходит первый 1 - компьютер или 2 - игрок:")
    while not (whose_move in ['1', '2']):
        whose_move = input("Кто ходит первый 1 - компьютер или 2 - игрок:")
    whose_move = int(whose_move)

    if whose_move == 2:
        motion += 1

    while candies > 0:
        print(f'Осталось {candies} конфет')
        if motion % 2 == 0 and motion != 1:
            temp_val = int(
                input("Игрок, введите количество конфет:"))
            while not (0 < temp_val < 28):
                temp_val = int(
                    input(f"{name_player2}, введите корректное количество конфет!:"))
        else:
            if difficulty_level == 1:
                temp_val = random.randint(0, 29)
                print(f'Компьютер берет {temp_val} конфет')
                candies -= temp_val
            # elif difficulty_level == 2:




        
        if candies <= 0:
            if motion % 2 == 0:
                print(f"{name_player2}, вы победили")
            else:
                print(f"{name_player1}, вы победили")
        motion += 1


elif number_of_players == 2:
    name_player1 = str(input("Введите имя первого игрока:"))
    name_player2 = str(input("Введите имя второго игрока:"))

    while candies > 0:
        print(f'Осталось {candies} конфет')
        if motion % 2 == 0 and motion != 1:
            temp_val = int(input("Второй игрок, введите количество конфет:"))
            while not (0 < temp_val < 28):
                temp_val = int(
                    input(f"{name_player2}, введите корректное количество конфет!:"))

        else:
            temp_val = int(input("Первый игрок, введите количество конфет:"))
            while not (0 < temp_val < 28):
                temp_val = int(
                    input(f"{name_player1}, введите корректное количество конфет!:"))

        candies -= temp_val
        if candies <= 0:
            if motion % 2 == 0:
                print(f"{name_player2}, вы победили")
            else:
                print(f"{name_player1}, вы победили")
        motion += 1
