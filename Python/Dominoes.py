print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
import random


def create_game_bank(domino_bank, status):
    game_bank = []
    game_bank.extend(domino_bank)
    random.shuffle(game_bank)
    stock_pieces = []
    for i in range(14):
        stock_pieces.extend([random.choice(game_bank)])
        game_bank.remove(stock_pieces[i])
    random.shuffle(stock_pieces)
    computer_pieces = []
    for j in range(7):
        computer_pieces.extend([random.choice(game_bank)])
        game_bank.remove(computer_pieces[j])
    random.shuffle(computer_pieces)
    player_pieces = []
    for k in range(7):
        player_pieces.extend([random.choice(game_bank)])
        game_bank.remove(player_pieces[k])
    random.shuffle(player_pieces)
    computer_counter = 0
    for m in computer_pieces:
        if m[0] + m[1] >= computer_counter:
            computer_counter = m[0] + m[1]
    player_counter = 0
    for p in player_pieces:
        if p[0] + p[1] >= player_counter:
            player_counter = p[0] + p[1]
    if computer_counter > player_counter:
        for cc in computer_pieces:
            if cc[0] + cc[1] == computer_counter:
                fdom = [cc]  # []
                computer_pieces.remove(cc)
        status = 'player'
        status_msg = "It's your turn to make a move. Enter your command."
    else:
        for pc in player_pieces:
            if pc[0] + pc[1] == player_counter:
                fdom = [pc]  # []
                player_pieces.remove(pc)
        status = 'computer'
        status_msg = "Computer is about to make a move. Press Enter to continue..."
    domino_snake = []
    domino_snake.extend(fdom)
    printer(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)


def game(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg):
    while True:
        x = input()
        if status == 'computer' and x == '':
            break
        elif status == 'computer' and x not in '':
            print('Invalid input. Please try again.')
        elif status == 'computer' and x == '':
            break
        elif status == 'player' and x not in '0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21':
            print('Invalid input. Please try again.')
        elif x == '-' or x == ' ' or x == '':
            print('Invalid input. Please try again.')
        elif len(player_pieces) >= int(x) >= -len(player_pieces):
            x = int(x)
            break
        else:
            print('Invalid input. Please try again.')

    if status == 'player':
        if x > 0 and not domino_snake[-1][-1] in player_pieces[x-1]:
            print('Illegal move. Please try again.')
            game(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)
        elif x > 0 and domino_snake[-1][-1] in player_pieces[x - 1]:
            if player_pieces[x-1][0] != domino_snake[-1][-1]:
                changer = player_pieces[x-1][0]
                player_pieces[x-1][0] = player_pieces[x-1][1]
                player_pieces[x-1][1] = changer
            else:
                pass
            domino_snake.append(player_pieces[x - 1])
            player_pieces.remove(player_pieces[x - 1])
        if x < 0 and not domino_snake[0][0] in player_pieces[abs(x)-1]:
            print('Illegal move. Please try again.')
            game(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)
        elif x < 0 and domino_snake[0][0] in player_pieces[abs(x)-1]:
            if player_pieces[abs(x) - 1][1] != domino_snake[0][0]:
                changer = player_pieces[abs(x) - 1][1]
                player_pieces[abs(x) - 1][1] = player_pieces[abs(x) - 1][0]
                player_pieces[abs(x) - 1][0] = changer
            else:
                pass
            domino_snake.insert(0, player_pieces[abs(x) - 1])
            player_pieces.remove(player_pieces[abs(x) - 1])
        elif x == 0:
            if len(stock_pieces) > 0:
                player_pieces.append(random.choice(stock_pieces))
                stock_pieces.remove(player_pieces[-1])
            else:
                status_domino(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)

    elif status == 'computer':
        # >>>>>>  PRIORITY  >>>>>
        rating_list = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        del_list = domino_snake + computer_pieces
        for_count = []
        for i in del_list:
            for j in i:
                for_count.append(j)
        for j in range(len(rating_list)):
            rating_list[j] = for_count.count(j)
        exchange = []
        for k in computer_pieces:
            exchange.append(rating_list[k[0]] + rating_list[k[1]])
        priority = []
        main_priority = []
        while len(exchange) > 0:
            counter = 0
            if sum(exchange) == 0:
                main_priority.append(0)
                break
            for i in exchange:
                if i >= counter:
                    counter = i
            priority.append(exchange.index(counter))
            main_priority.append(exchange.index(counter) + 1)
            main_priority.append(-(exchange.index(counter) + 1))
            exchange[exchange.index(counter)] = 0
        #  <<<<<  PRIORITY  <<<<<

        while True:
            if len(main_priority) == 0:
                main_priority.append(0)
            x = main_priority[0]
            main_priority.remove(x)
            if x > 0 and domino_snake[-1][-1] in computer_pieces[x - 1]:
                if computer_pieces[x - 1][0] != domino_snake[-1][-1]:
                    changer = computer_pieces[x - 1][0]
                    computer_pieces[x - 1][0] = computer_pieces[x - 1][1]
                    computer_pieces[x - 1][1] = changer
                domino_snake.append(computer_pieces[x - 1])
                computer_pieces.remove(computer_pieces[x - 1])
                status_domino(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)
            elif x < 0 and domino_snake[0][0] in computer_pieces[abs(x) - 1]:
                if computer_pieces[abs(x) - 1][1] != domino_snake[0][0]:
                    changer = computer_pieces[abs(x) - 1][1]
                    computer_pieces[abs(x) - 1][1] = computer_pieces[abs(x) - 1][0]
                    computer_pieces[abs(x) - 1][0] = changer
                domino_snake.insert(0, computer_pieces[abs(x) - 1])
                computer_pieces.remove(computer_pieces[abs(x) - 1])
                status_domino(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)
            elif x == 0:
                if len(stock_pieces) > 0:
                    computer_pieces.append(random.choice(stock_pieces))
                    stock_pieces.remove(computer_pieces[-1])
                    status_domino(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)
                else:
                    status_domino(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)
    status_domino(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)


def status_domino(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg):
    if status == 'player':
        status = 'computer'
        status_msg = "Computer is about to make a move. Press Enter to continue..."
    else:
        status = 'player'
        status_msg = "It's your turn to make a move. Enter your command."
    if len(player_pieces) == 0:
        status_msg = "The game is over. You won!"
    elif len(computer_pieces) == 0:
        status_msg = "The game is over. The computer won!"
    elif domino_snake[-1][-1] == domino_snake[0][0]:
        game_end_counter = 0
        for i in domino_snake:
            for j in i:
                if j == domino_snake[-1][-1]:
                    game_end_counter += 1
        if game_end_counter == 8:
            status_msg = "The game is over. It's a draw!"
    printer(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)


def printer(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg):
    print('=' * 70)
    print(f'Stock size: {len(stock_pieces)}')
    print(f'Computer pieces: {len(computer_pieces)}\n')
    if len(domino_snake) > 6:
        first = domino_snake[0:3]
        dots = '...'
        second = domino_snake[-3:]
        print(*first, sep='', end='')
        print(*dots, sep='', end='')
        print(*second, sep='', end='\n\n')
    else:
        print(*domino_snake, sep='', end='\n\n')
    print('Your pieces:')
    for i in range(len(player_pieces)):
        print(f'{i + 1}: {player_pieces[i]}')
    print()
    print(f'Status: {status_msg}')
    if 'The game is over' in status_msg:
        exit()
    else:
        game(stock_pieces, computer_pieces, player_pieces, domino_snake, status, status_msg)


def main():
    domino_bank = [[i, j] for i in range(7) for j in range(i, 7)]
    status = ''
    create_game_bank(domino_bank, status)


main()
