from random import randint
from random import choice


def saver(x, result, lvl):
    gamemode = {'1': 'simple operations with numbers 2-9',
                '2': 'integral squares of 11 - 29'}
    if input() in answers:
        name = input('What is your name?')
        file = open('[ARI]results.txt', 'a')
        file.write(f"\n{name}: {memory.count('Right!')}/5 in level {lvl} ({gamemode[str(lvl)]}).")
        file.close()
        print('The results are saved in "[ARI]results.txt".')
        main()
    else:
        main()


def mode():
    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9\n2 - integral squares of 11 - 29')
    lvl = input()
    if lvl not in ['1', '2']:
        print('Incorrect format.')
        mode()
    else:
        create_task(lvl)


def create_task(lvl):
    oper = ['+', '-', '*']
    if lvl == '1':
        task = [str(randint(2, 9)) + ' ' + choice(oper) + ' ' + str(randint(2, 9))]
        result = eval(task[0])
        print(*task)
        start(result, lvl)
    else:
        task = randint(11, 29)
        result = task * task
        print(task)
        start(result, lvl)


def end(x, result, lvl):
    print('Right!' if str(x) == str(result) else 'Wrong!')
    memory.append('Right!' if str(x) == str(result) else 'Wrong!')
    if len(memory) == 5:
        print(f"Your mark is {memory.count('Right!')}/5. ",end='')
        print('Would you like to save the result? Enter yes or no.')
        saver(x, result, lvl)
    else:
        create_task(lvl)


def start(result, lvl):
    x = input()
    if '-' in x:
        x = x.replace('-', '')
        if x.isdigit():
            x = -int(x)
            end(x, result, lvl)
    if x.isdigit():
        end(x, result, lvl)
    else:
        print('Wrong format! Try again.')
        start(result, lvl)


def main():
    global memory
    memory = []
    global answers
    answers = ['y', 'yes', 'YES', 'Yes']
    if input('Do you want to see stat log?\n') in answers:
        file = open('[ARI]results.txt', 'r')
        content = file.read()
        print(content)
        file.close()
    print()
    if input('Are you ready?\n') in answers:
        print()
        mode()
    else:
        exit()

main()
