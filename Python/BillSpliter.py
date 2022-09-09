import random
print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
friends = {}
print("Enter the number of friends joining (including you):")
x = int(input())

if x <= 0:
    print("\nNo one is joining for the party")
elif x > 0:
    print("Enter the name of every friend (including you), each on a new line:")

    for i in range(x):
        friends[f"{input()}"] = 0

    print('Enter the total bill value:')
    total = float(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    ask = input()

    if ask != 'Yes':
        print('No one is going to be lucky')
        slices = round(total / x, 2)
        friends = dict.fromkeys(friends, slices)
        print(friends)
    else:
        racho = random.choice(list(friends))
        print(f'{racho} is the lucky one!')
        slices = round(total / (x - 1), 2)
        friends = dict.fromkeys(friends, slices)
        friends.update([(racho, 0)])
        print(friends)