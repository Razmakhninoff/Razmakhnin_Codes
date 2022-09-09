m = 0  # Main Matrix
er = ''


def check_board():
    b = input("Enter your board dimensions: ").split()
    d = not b[0].isdigit() or not b[-1].isdigit()
    if len(b) != 2 or d is True or b[0] == '0' or b[-1] == '0':
        print('Invalid dimensions!')
        check_board()
    else:
        global bx, by, m, us, u, grid
        bx = int(b[0])  # Board x-vector
        by = int(b[-1])  # Board y-vector
        us = "_" * len(str(bx * by))
        m = [[us for _ in range(bx + 1)] for _ in range(by + 1)]
        u = len(str(bx * by))
        grid = [['_' * u] * bx for _ in range(by)]
        main()


def check_position():
    k = input("Enter the knight's starting position: ").split()
    d = not k[0].isdigit() or not k[-1].isdigit()
    if len(k) != 2 or d is True or k[0] == '0' or k[-1] == '0':
        print('Invalid position!')
        check_position()
    elif int(k[0]) > bx or int(k[-1]) > by:
        print('Invalid position!')
        check_position()
    else:
        global kx, ky, us2
        kx = int(k[0])  # Knight x-vector
        ky = int(k[-1])  # Knight y-vector
        us2 = " " * (int(len(str(bx * by))) - 1)
        m[ky][kx] = us2 + "X"
        switcher()


def switcher():
    puzzle = input('Do you want to try the puzzle? (y/n): ')
    if puzzle not in 'yn':
        print('Invalid input')
        switcher()
    elif puzzle == 'y':
        if not algo_solver(grid, bx, by, kx, ky, u, 1):
            print("No solution exists!")
        else:
            check_moves()
    else:
        solver()


def check_moves():
    global possible
    possible = [[ky - 2, kx + 1], [ky + 2, kx + 1],
                [ky + 1, kx + 2], [ky + 2, kx - 1],
                [ky + 1, kx - 2], [ky - 2, kx - 1],
                [ky - 1, kx - 2], [ky - 1, kx + 2]]
    for i in possible:
        if 0 < i[0] <= by and 0 < i[1] <= bx and m[i[0]][i[1]] != us2 + '*':
            m[i[0]][i[1]] = us2 + "0"
            count = 0
            pky = i[0]
            pkx = i[1]
            pm = [[pky - 2, pkx + 1], [pky + 2, pkx + 1],
                  [pky + 1, pkx + 2], [pky + 2, pkx - 1],
                  [pky + 1, pkx - 2], [pky - 2, pkx - 1],
                  [pky - 1, pkx - 2], [pky - 1, pkx + 2]]
            for j in pm:
                if 0 < j[0] <= by and 0 < j[1] <= bx:
                    if m[j[0]][j[1]] == us:
                        count += 1
            m[i[0]][i[1]] = us2 + str(count)
        else:
            continue
    po_move = [us2 + '0', us2 + '1', us2 + '2', us2 + '3', us2 + '4', us2 + '5',
               us2 + '6', us2 + '7', us2 + '8', us2 + '9']
    global mo_count
    mo_count = 0
    for i in m:
        for j in i:
            if j in po_move:
                mo_count += 1
    printer()


def printer():
    t = int(len(str(bx * by)))
    bn = bx * (len(str(bx * by)) + 1) + 3
    border = (" " * len(str(by))) + "-" * bn
    wsn = "  " * t
    if t < 2:
        wsn = "   " * t
    n = []
    for i in range(1, bx + 1):
        if i < 9:
            n.append(str(i) + " " * t)
        elif 99 > i >= 9:
            n.append(str(i) + " " * (t - 1))
        elif i >= 99:
            n.append(str(i) + " " * (t - 2))
    n[-1] = bx
    # Print Board >>>
    print(border)
    for i in range(by, 0, -1):
        s = ' '
        if len(str(i)) >= 2 or len(str(by)) < 2:
            s = ''
        print(f"{s}{i}| {' '.join(m[i][1:999])} |")
    print(border)
    print(wsn, *n, sep='')
    if mo_count != 0:
        replacer()
    else:
        end()


def next_move():
    global er
    te2 = us2 + '*'
    n = input(f"{er}Enter your next move: ").split()
    d = not n[0].isdigit() or not n[-1].isdigit()
    if len(n) != 2 or d is True or n[0] == '0' or n[-1] == '0':
        er = 'Invalid move! '
        next_move()
    elif int(n[0]) > bx or int(n[-1]) > by:
        er = 'Invalid move! '
        next_move()
    elif m[int(n[-1])][int(n[0])] == te2:
        er = 'Invalid move! '
        next_move()
    elif [int(n[-1]), int(n[0])] not in possible:
        er = 'Invalid move! '
        next_move()
    else:
        global kx, ky
        er = ''
        kx = int(n[0])  # Knight x-vector
        ky = int(n[-1])  # Knight y-vector
        m[ky][kx] = us2 + "X"
        check_moves()


def replacer():
    for i in range(by + 1):
        for j in range(bx + 1):
            if m[i][j] == us2 + 'X':
                m[i][j] = us2 + '*'
    cleaner()


def cleaner():
    for i in range(by + 1):
        for j in range(bx + 1):
            if m[i][j] != us2 + '*':
                m[i][j] = us
    print()
    next_move()


def end():
    squares = bx * by  # - 1
    sq_count = 1
    for i in range(by + 1):
        for j in range(bx + 1):
            if m[i][j] == us2 + '*':
                sq_count += 1
    if sq_count >= squares:
        print('What a great tour! Congratulations!')
        exit()
    else:
        print('No more possible moves!')
        print(f'Your knight visited {sq_count} squares!')
        exit()


def find_solver(grid, bx, by, kx, ky, u):
    pos = solver_searcher(grid, bx, by, kx, ky)
    for item in pos:
        way = len(solver_searcher(grid, bx, by, item[0], item[1])) - 1
        grid[item[1] - 1][item[0] - 1] = ' ' * (u - 1) + str(way)
    return pos


def algo_solver(grid, bx, by, kx, ky, u, step):
    grid[ky - 1][kx - 1] = ' ' * (u - 1) + str(step)
    if step == bx * by:
        return True
    pos = solver_searcher(grid, bx, by, kx, ky)
    for item in pos:
        if algo_solver(grid, bx, by, item[0], item[1], u, step + 1):
            return True
    grid[ky - 1][kx - 1] = '_' * u
    return False


def solver_printer(grid, bx, by, kx, ky, u):
    place = len(str(by))
    line = ' ' * place + '-' * (bx * (u + 1) + 3)
    print(line)
    info = "{:>" + f"{place}}}| " + "{} " * bx + "|"
    for i in range(by, 0, -1):
        print(info.format(i, *grid[i - 1]))
    print(line)
    end = ' ' * u
    for i in range(1, bx + 1):
        end += ' ' * u + str(i)
    print(end)


def solver_searcher(grid, bx, by, kx, ky):
    dir_x = [-2, -2, 2, 2, -1, 1, -1, 1]
    dir_y = [-1, 1, -1, 1, -2, -2, 2, 2]
    pos = []
    for i in range(8):
        new_x = kx + dir_x[i]
        new_y = ky + dir_y[i]
        if check(new_x, new_y, bx, by) and '_' in grid[new_y - 1][new_x - 1]:
            pos.append((new_x, new_y))
    return pos


def check(kx, ky, bx, by):
    return 1 <= kx <= bx and 1 <= ky <= by


def solver():
    print()
    if not algo_solver(grid, bx, by, kx, ky, u, 1):
        print("No solution exists!")
    else:
        print("Here's the solution!")
        solver_printer(grid, bx, by, kx, ky, u)


def main():
    if m == 0:
        check_board()
    else:
        check_position()


main()
