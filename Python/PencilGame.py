#  RULES\  #
print('Hello there!\n\n\nGAMEMODES:')
print(' 1. Hard Jack Mode - with bot\n 2. Original Mode - without bot\n')
print('RULES:\n> Only 2 players — John and Jack\n> Who will remove last pencil - lose')
print('> You can remove only 1 - 3 pencil / turn\n\n\n>>>>>>>>>>>>')
#  /RULES  #
print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
print("Do you want to play with bot?('+' or '-')")

gamemode = ['+', '-']
bot = gamemode[0]
original = gamemode[1]
pressbot = input()

while True:
    if pressbot == bot or pressbot == original:
        break
    if pressbot != bot or pressbot != original:
        print("Choose between " + "'" + bot + "'" + " and " + "'" + original + "'");
        pressbot = input()

if pressbot == bot:

    print('Bot Jack joined the game\n••••••••••••••')
    print('Hard Jack Mode\n>>>>>>>>>>>>\n')

    print('How many pencils would you like to use')
    while True:
        try:
            number = int(input())
        except ValueError:
            print('The number of pencils should be numeric')
        else:
            if number < 0:
                print('The number of pencils should be numeric')
                continue
            elif number == 0:
                print('The number of pencils should be positive')
            elif number != 0 and number > 0:
                break

    names = ['John', 'Jack']
    a = names[0]
    b = names[1]
    name = input('Who will be the first (' + a + ', ' + b + ')\n')

    while True:
        if name == a or name == b:
            break
        if name != a or name != b:
            print('Choose between ' + a + ' and ' + b)
            name = input()

    while number > 0:
        print('|' * number)
        print(name + "'s turn!")

        #  \\----------- BOT LOGIC -------------\\  #

        # Jack is always bot

        if name == b:
            if number == 1:
                entered = 1
                print(entered)
                number -= entered
                print(a + ' won!')
                break
            elif number % 4 == 0:
                entered = 3
                print(entered)
                number -= entered
                name = 'John' if name == 'Jack' else 'Jack'
                print('|' * number)
                print(name + "'s turn!")
            elif number % 4 == 3:
                entered = 2
                print(entered)
                number -= entered
                name = 'John' if name == 'Jack' else 'Jack'
                print('|' * number)
                print(name + "'s turn!")
            elif number % 4 == 2:
                entered = 1
                print(entered)
                number -= entered
                name = 'John' if name == 'Jack' else 'Jack'
                print('|' * number)
                print(name + "'s turn!")
            elif number % 4 == 1:
                entered = 1
                print(entered)
                number -= entered
                name = 'John' if name == 'Jack' else 'Jack'
                print('|' * number)
                print(name + "'s turn!")

        #  //----------- BOT LOGIC -------------//  #

        while True:
            try:
                entered = int(input())
            except ValueError:
                print("Possible values: '1', '2' or '3'")
            else:
                break

        number -= entered
        name = 'John' if name == 'Jack' else 'Jack'
        while entered <= 0 or entered > 3:
            print("Possible values: '1', '2' or '3'")
            number += entered

            while True:
                try:
                    entered = int(input())
                except ValueError:
                    print("Possible values: '1', '2' or '3'")
                else:
                    break

            number -= entered
        while number < 0:
            print('Too many pencils were taken')
            number += entered

            while True:
                try:
                    entered = int(input())
                except ValueError:
                    print("Possible values: '1', '2' or '3'")
                else:
                    break

            number -= entered
        while number == 0:
            print(name + ' won!')
            break

#  //----------- Original Mode -------------//  # 

elif pressbot == original:

    print('Bot Jack left the game\n••••••••••••••')
    print('Original Mode\n>>>>>>>>>>>>\n')

    print('How many pencils would you like to use?')
    while True:
        try:
            number = int(input())
        except ValueError:
            print('The number of pencils should be numeric')
        else:
            if number < 0:
                print('The number of pencils should be numeric')
                continue
            elif number == 0:
                print('The number of pencils should be positive')
            elif number != 0 and number > 0:
                break

    names = ['John', 'Jack']
    a = names[0]
    b = names[1]
    name = input('Who will be the first (' + a + ', ' + b + ')\n')

    while True:
        if name == a or name == b:
            break
        if name != a or name != b:
            print('Choose between ' + a + ' and ' + b)
            name = input()

    while number > 0:
        print('|' * number)
        print(name + "'s turn!")

        while True:
            try:
                entered = int(input())
            except ValueError:
                print("Possible values: '1', '2' or '3'")
            else:
                break

        number -= entered
        name = 'John' if name == 'Jack' else 'Jack'
        while entered <= 0 or entered > 3:
            print("Possible values: '1', '2' or '3'")
            number += entered

            while True:
                try:
                    entered = int(input())
                except ValueError:
                    print("Possible values: '1', '2' or '3'")
                else:
                    break

            number -= entered
        while number < 0:
            print('Too many pencils were taken')
            number += entered

            while True:
                try:
                    entered = int(input())
                except ValueError:
                    print("Possible values: '1', '2' or '3'")
                else:
                    break

            number -= entered
        while number == 0:
            print(name + ' won!')
            break

print("\n\nThx for game!\nGood Luck, friend!")
