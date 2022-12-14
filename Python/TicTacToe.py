m = [
    ['0', '0', '0', '0'],
    ['0', ' ', ' ', ' '],  # 11 12 13
    ['0', ' ', ' ', ' '],  # 21 22 23
    ['0', ' ', ' ', ' ']   # 31 32 33
    ]

count = 1   # count for switch X O
cosymb = 0  # count symbols

def wins(x):
    tab = ['XXX', 'OOO']
    if (m[1][1] + m[1][2] + m[1][3] in tab) or (m[1][1] + m[2][1] + m[3][1] in tab):
        print(f'{m[1][1]} wins')
    elif (m[1][3] + m[2][3] + m[3][3] in tab) or (m[3][3] + m[3][2] + m[3][1] in tab):
        print(f'{m[3][3]} wins')
    elif (m[1][2] + m[2][2] + m[3][2] in tab) or (m[2][1] + m[2][2] + m[2][3] in tab):
        print(f'{m[2][2]} wins')
    elif (m[1][3] + m[2][2] + m[3][1] in tab) or (m[1][1] + m[2][2] + m[3][3] in tab):
        print(f'{m[2][2]} wins')
    else:
        main()

def grid(x):
    if m[int(x[0])][int(x[-1])] != ' ':  # (func checker third step)
        print('This cell is occupied! Choose another one!')
        main()
    global count
    global cosymb
    if count % 2 == 1:
        m[int(x[0])][int(x[-1])] = 'X'
        cosymb += 1
    elif count % 2 == 0:
        m[int(x[0])][int(x[-1])] = 'O'
        cosymb += 1
    count += 1
    print(f"""
---------
| {m[1][1]} {m[1][2]} {m[1][3]} |
| {m[2][1]} {m[2][2]} {m[2][3]} |
| {m[3][1]} {m[3][2]} {m[3][3]} |
---------
""")
    wins(x)

def checker(x):
    if not x[0].isdigit() or not x[-1].isdigit():
        print('You should enter numbers!')
        main()
    elif x[0] not in '123' or x[-1] not in '123':
        print('Coordinates should be from 1 to 3!')
        main()
    else:
        grid(x)

def start():
    x = '         '
    print(f"""
---------
| {x[0]} {x[1]} {x[2]} |
| {x[3]} {x[4]} {x[5]} |
| {x[6]} {x[7]} {x[8]} |
---------
""")
    main()

def main():
    if cosymb != 9:
        x = input()
        checker(x)
    elif cosymb == 9:
        print("Draw")
        exit()
print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
print('Write coordinates X,Y ...\nlike a 1 1, 2 3')
start()
