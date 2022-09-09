
import random
# /WIN DIC/
w = {
    'water' : ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
    }
# /WIN DIC/
classic = ['rock', 'scissors', 'paper']
valid = []  # Valid inputs
sb = {}     # ScoreBoard
stat = {'win': 100, 'draw': 50}
print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
name = input('Enter your name: ')
print(f'Hello, {name}')
with open('[RPC]rating.txt') as rate:
    for line in rate:
        key, value = line.split()
        sb[key] = value
if name not in sb:
    sb[name] = 0
# /OPTIONS/
option = input()
if option == '':
    valid = classic
elif option != '':
    option = option.split(',')
    for i in option:
        valid.append(i)
print("Okay, let's start")
# /OPTIONS/

while True:
    x = input()
    y = random.choice(valid)
    if x == '!exit':
        print('Bye!')
        break
    elif x == '!rating':
        print(f'Your rating: {sb[name]}')
    elif x not in valid:
        print('Invalid input')
    elif x == y:
        print(f'There is a draw ({x})')
        sb[name] = int(sb[name]) + int(stat['draw'])
    elif y in w[x] and x not in w[y]:
        print(f'Well done. The computer chose {y} and failed')
        sb[name] = int(sb[name]) + int(stat['win'])
    elif x in w[y] and y not in w[x]:
        print(f'Sorry, but the computer chose {y}')